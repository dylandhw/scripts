import requests 
import pyttsx3 
from gtts import gTTS
import os

def check_internet(url="https://www.google.com", timeout=5):
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False 
    except requests.Timeout:
        return False 

def googleTTS():
    text = "hello world. google text-to-speech has given me life!"
    tts = gTTS(text)
    tts.save("hello.mp3")
    os.system("mpg123 hello.mp3")

def localTTS():
    engine = pyttsx3.init()
    engine.say("hello, world. python has given me life!")
    engine.runAndWait()

def main():
    if check_internet():
        googleTTS()
    else:
        localTTS()

if __name__ == "__main__":
    main()