import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import stt_api



def record_audio():
    input_device = 9

    fs=44100
    duration = 5  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64' , device=input_device)
    print ("Recording Audio")
    sd.wait()
    print ("Audio recording complete")
    #sd.play(myrecording, fs)
    wav.write('output.wav', fs, myrecording)
    sd.wait()
    #print ("Play Audio Complete")



"""fs = 44100
duration = 10
threshold = 0.01
input_device = 9

#initialise variables
frames = []

def audio_callback(indata, frames, time, status):
    global recording
    if np.max(indata) > threshold:
        if not recording:
            print("start recording")
            recording = True
        frames.append(indata)
    else:
        if recording:
            print("stop recording")
            recording = False

def audio_stream():
    stream = sd.InputStream(callback=audio_callback, channels=2, samplerate=fs, device=input_device)
    stream.start()

    # Wait for microphone activity
    while not recording:
        pass

    # Continue recording until there is no activity for a specified duration
    while True:
        if not recording:
            break

    # Stop audio stream
    stream.stop()
    stream.close()

    # Concatenate recorded frames
    myrecording = np.concatenate(frames)

    # Save recorded audio to a WAV file
    wav.write('output.wav', fs, myrecording)"""
