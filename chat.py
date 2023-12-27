import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() 
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  }
]

model = genai.GenerativeModel('gemini-pro',generation_config=generation_config,safety_settings=safety_settings)

chat = model.start_chat()

while True:
    response = chat.send_message(input("You:"))
    output=response.text
    print("Geminiai",output)
    

