import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
load_dotenv() 
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel('gemini-pro-vision',generation_config=generation_config,safety_settings=safety_settings)

img = PIL.Image.open('image.jpg')
response = model.generate_content([input("You:"), img])
output=response.text
print("Geminiai:", output)


