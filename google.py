import utils

def transcribe_gcs(text_file, gcs_uri: str) -> str:
    """Asynchronously transcribes the audio file specified by the gcs_uri.

    Args:
        gcs_uri: The Google Cloud Storage path to an audio file.

    Returns:
        The generated transcript from the audio file provided.
    """
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    response = operation.result(timeout=90)

    transcript_builder = []
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        transcript_builder.append(f"{result.alternatives[0].transcript}")

    text = "".join(transcript_builder)
    text_file.write(text)
    text_file.close()

    print("completed", gcs_uri, "\n\n")


def main():
    file_names = utils.get_file_names("/Users/andressanchez/Dropbox/Mac/Desktop/participant_files/snippets")
    # file_names = ['s101_1.wav', 'd103_4.wav']

    for name in file_names:
        # handle filenames for different tasks to make gcs_uri
        if name[0] != "s":
            gcs_uri = 'gs://clean_gt_snippets/snippets/s' + name[1:4] + '/s' + name[1:6] + '/' + name
        else:
            gcs_uri = 'gs://clean_gt_snippets/snippets/' + name[:4] + '/' + name

        # open text files in correct folder
        text_file = open('/Users/andressanchez/Dropbox/Mac/Desktop/ggl_transcripts_raw/' + name[1:4] + '/ggl_' + name[:-4] + '.txt','w')
        transcribe_gcs(text_file, gcs_uri)
        
if __name__ == '__main__':
    main()