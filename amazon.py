import os
import boto3
import time
import urllib
import json

transcribe_client = boto3.client('transcribe')
text_file = open('/Users/andressanchez/Dropbox/Mac/Desktop/amazon_s101_3.txt','w')

def transcribe_file(job_name, file_uri, transcribe_client):
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
                response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                data = json.loads(response.read())
                text = data['results']['transcripts'][0]['transcript']
                text_file.write(job_name[0] + '\n' + text + '\n\n\n')
            break

def get_file_names():
    path ="/Users/andressanchez/Dropbox/Mac/Desktop/participant_files/snippets/s101/s101_3"
    #we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list
            filelist.append(file)

    return sorted(filelist)

def main():
    files = get_file_names()

    for f in files:
        file_uri = 's3://dva-asr-bias/s101_3/' + f
        job_name = f
        transcribe_file(job_name, file_uri, transcribe_client)


if __name__ == '__main__':
    main()