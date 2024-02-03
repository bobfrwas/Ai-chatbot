# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

def call_api(file):

    aai.settings.api_key = "78cb8d9d128a4efd8b6917cabf79460b"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(file)
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    return(transcript.text)