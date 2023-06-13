import os
import boto3
import time
import urllib
import json

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

def get_file_names():
    path ="/Users/andressanchez/Dropbox/Mac/Desktop/participant_files/snippets"
    #we shall store all the file names in this list
    filelist = []

    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list
            if "DS" not in file:
                filelist.append(file)

    return sorted(filelist)

def main():
    file_names = get_file_names()
    # file_names = ["s104_1.wav", "s104_2h.wav", "s104_2s.wav", "s105_1.wav", "s105_2h.wav", "s105_2s.wav"]

    for name in file_names:
        job_name = "v3_" + name

        if name[0] != "s":
            file_uri = 's3://dva-asr-bias/snippets/s' + name[1:4] + '/s' + name[1:6] + '/' + name
        else:
            file_uri = 's3://dva-asr-bias/snippets/' + name[:4] + '/' + name

        text_file = open('/Users/andressanchez/Dropbox/Mac/Desktop/amazon_transcripts/' + name[1:4] + '/ama_' + name[:-4] + '.txt','w')
        transcribe_file(job_name, file_uri, transcribe_client, text_file)
        
if __name__ == '__main__':
    main()