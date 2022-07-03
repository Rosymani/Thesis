import random
import time
import warnings
import pyttsx3
import speech_recognition as sr  # recognise speech
from gtts import gTTS  # Google text to speech
import playsound   # to play an audio file
import os    # to remove created audio files
import random
import requests

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(audio)
    engine.runAndWait()


r = sr.Recognizer()  # Intialise a recogniser
# Listen for audio and convert it to text:

def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source,5,5)  # listen the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  #convert audio to text

        except sr.UnknownValueError:
             engine_speak('I did not get that ')

        except sr.RequestError:
             engine_speak('Request Error from Google speech Recognition')  # error : recognizer is not connected

        print(">>",voice_data.lower())  # print what user said
        return voice_data.lower()

# get string and make a audio file to be played

def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1,200000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)  # play the audio file
    print(asis_obj.name + ":", audio_string)  # print what user said
    os.remove(audio_file)



def respond(voice_data):
    # Greetings
    if there_exists( ['hey','hi','hello']):
        greetings = ["hello, how can I help you " + person_obj.name, "hello, whats up?" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    if there_exists(["how are you", "how are you doing "]):
        greetings = (" I am very well, Thanks for asking" + person_obj.name , "I am too good " + person_obj.name )
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)



time.sleep(1)
person_obj = person()
asis_obj = asis()
asis_obj.name = 'kibi'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording")  # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)