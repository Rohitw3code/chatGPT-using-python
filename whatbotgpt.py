import os
import openai
import pyttsx3

engine = pyttsx3.init()

openai.api_key = "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"#os.getenv("OPENAI_API_KEY")


def insert_newline(string):
  if len(string) > 100:
    newString = ""
    for i in range(len(string)):
      if string[i] == " " and (i + 1) % 100 == 0:
        newString += '\n'
      else:
        newString += string[i]
    return newString
  return string

def nextLine(myString):
  if len(myString) > 100:
    myString = myString[:100] + "\n" + myString[100:]
  return myString


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
while True:
  msg = str(input("Human: "))
  text+="\nHuman: "+msg+"\nAI:"
  ai = aiResponse(text).strip()
  engine.say(ai)
  engine.runAndWait()
  print("AI : ",nextLine(ai))
  print()
  text+=ai