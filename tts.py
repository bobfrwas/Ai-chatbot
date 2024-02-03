import pyttsx3

def text_to_speech(ai_response):
    engine = pyttsx3.init()
    engine.say(ai_response)
    engine.runAndWait()

