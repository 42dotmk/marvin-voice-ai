from ollama import Client
from RealtimeTTS import TextToAudioStream, SystemEngine

engine = SystemEngine() 
stream = TextToAudioStream(engine)

client = Client(host='https://llama.42.mk/')

def chat(text):
  print(text + " (sent to Llama)")
  for response in client.chat(
    model='llama2', 
    messages=[
      {
        'role': 'user',
        'content': text,
      },
    ],
    stream=True
  ):
    if (text_chunk := response['message']['content']) is not None: 
      yield text_chunk
