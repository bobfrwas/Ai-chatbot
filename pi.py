import record_mic , stt_api, ai, tts
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

record_mic.record_audio()
message = stt_api.call_api("output.wav")
ai_response = ai.chatbot(message)
tts.text_to_speech(ai_response)