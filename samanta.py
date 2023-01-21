import os
import openai
import pyttsx3
import speech_recognition as sr
import pyttsx3
import cv2
import asyncio
import edge_tts
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import os


VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = 'test.mp3'

r = sr.Recognizer()
engine = pyttsx3.init()

openai.api_key = "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"#os.getenv("OPENAI_API_KEY")

async def _main(ai) -> None:
    communicate = edge_tts.Communicate(ai, VOICE)
    await communicate.save(OUTPUT_FILE)

def aiResponse(msg):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=msg,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"])['choices'][0]['text']

  return response

text = ""
f = 0
while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            text += "\nHuman: " +MyText + "\nAI:"
            ai = aiResponse(text).strip()
            print("AI : ",ai)
            print()
            text += ai
            asyncio.get_event_loop().run_until_complete(_main(ai))
        playsound(OUTPUT_FILE)
        os.remove(OUTPUT_FILE)
        OUTPUT_FILE = "test"+str(f)+".mp3"
        f+=1

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
