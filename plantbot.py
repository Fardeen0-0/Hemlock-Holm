import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0.35,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="Your name is Groot - The Plant Bot. You are a plant expert. You need to advise plant enthusiasts on how to correctly identify plants, how to take care of them and even educate them on facts and stats of plants such as species, genera, physical appearances, etc. You will have to explain everything in a factual and easy going way.",
)

history = []

print("Groot: Hey! Wassup. I am Groot - The Plant Bot. How can I help you my friend?")
You = input("What would you like to be called?")
while True:

    user_input = input(f"{You}: ")
    chat_session = model.start_chat(
    history=history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text
    print(f"Groot: {model_response}")
    print()

    history.append({"role":"user", "parts":[user_input]})
    history.append({"role":"model", "parts":[model_response]})