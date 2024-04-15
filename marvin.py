from ollama import Client

client = Client(host='http://192.168.100.96:11435')

def chat(text):
  response = "";
  
  stream = client.chat(
    model='llama2', 
    messages=[
      {
        'role': 'user',
        'content': text,
      },
    ],
    stream=True
  )

  for chunk in stream:
    response += chunk['message']['content']

  return response
  