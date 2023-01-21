import openai
import speech_recognition as sr
import edge_tts
import asyncio
from playsound import playsound
import os
import os

import edge_tts
import openai
import speech_recognition as sr
from playsound import playsound

# https://github.com/georgezhao2010/azure_cognitive_speech/blob/main/voice_list.json

VOICE = "hi-IN-SwaraNeural"
OUTPUT_FILE = 'test.mp3'

r = sr.Recognizer()

openai.api_key = os.getenv("OPENAI_API_KEY")

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
