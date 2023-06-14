import os
import boto3
import time
import urllib
import json
import utils

transcribe_client = boto3.client('transcribe')

def transcribe_file(job_name, file_uri, transcribe_client, text_file):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        LanguageCode='en-US'
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            if job_status == 'COMPLETED':
                print("completed " + job_name)
                response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                data = json.loads(response.read())
                text = data['results']['transcripts'][0]['transcript']
                text_file.write(text)
                text_file.close()
            break

def main():
    file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/participant_files/snippets")

    for name in file_names:
        # need new job names for every attempt
        job_name = "v3_" + name

        # handle filenames for different tasks to make s3 uri
        if name[0] != "s":
            file_uri = 's3://dva-asr-bias/snippets/s' + name[1:4] + '/s' + name[1:6] + '/' + name
        else:
            file_uri = 's3://dva-asr-bias/snippets/' + name[:4] + '/' + name

        # open text files in correct folder
        text_file = open('/Users/andressanchez/Dropbox/Mac/Desktop/amazon_transcripts/' + name[1:4] + '/ama_' + name[:-4] + '.txt','w')
        transcribe_file(job_name, file_uri, transcribe_client, text_file)
        
if __name__ == '__main__':
    main()