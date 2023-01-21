import os
import openai

openai.api_key = "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"#os.getenv("OPENAI_API_KEY")


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
  print(ai)
  text+=ai