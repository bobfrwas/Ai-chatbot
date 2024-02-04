import sounddevice as sd
import scipy.io.wavfile as wav
import stt_api
import numpy as np
import speech_recognition as sr
import pyaudio as pd
import math

import random
import time

import speech_recognition as sr

NOISE_THRESHOLD = 0
SILENCE_THRESHOLD = 0.5  # in seconds


def record_audio(recognizer, microphone):
    # Start recording audio when noise is detected
    with microphone as source:
        print("Listening for noise...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    return audio

def calculate_rms(audio):
    # Calculate root mean square (RMS) energy of the audio
    rms = math.sqrt(sum([sample ** 2 for sample in audio.frame_data]) / len(audio.frame_data))
    return rms

def transcribe_audio(recognizer, audio):
    # Transcribe the recorded audio
    try:
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Error: {}".format(e))
        return None

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        # Record audio when noise is detected
        audio = record_audio(recognizer, microphone)

        # Check if the recorded audio exceeds the noise threshold
        rms_energy = calculate_rms(audio)
        if rms_energy > NOISE_THRESHOLD:
            print("Noise detected!")

            # Wait for audio to become silent
            start_time = time.time()
            while rms_energy > SILENCE_THRESHOLD:
                audio = record_audio(recognizer, microphone)
                rms_energy = calculate_rms(audio)

                # Stop waiting if maximum silence threshold is reached
                if time.time() - start_time > SILENCE_THRESHOLD:
                    break

            # Transcribe the recorded audio when it becomes silent
            transcription = transcribe_audio(recognizer, audio)
            if transcription:
                print("Transcription: {}".format(transcription))
            else:
                print("No speech detected.")

        # Continue recording audio again
        print("Listening for noise...")
