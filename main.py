import os 
import google.generativeai as genai
from dotenv import load_dotenv

#load environment variable from .env file

load_dotenv()

#configure API key for Google Generative AI
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except AttributeError:
    print("Error! The GEMINI_API_KEY was not found.")
    exit()


#creating the generative model

model = genai.GenerativeModel('gemini-2.5-flash') #i've created an object here

#creating a chat session
chat = model.start_chat(history=[])

#main chat loop
print("Say Hello to Gemini-2.5-Flash! Type 'exit' to end the chat.")
print("=" * 50)

while True:
    user_input = input("You: ")

    if not user_input.strip():
        print("Gemini needs something to work with!")
        continue

    #check for exit
    if user_input.lower() == 'exit':
        print("\nThank you for chatting with Gemini!")
        break

    try:
        #user input is sent to the LLM
        response = chat.send_message(user_input, stream=True) 

        #printing LLM response
        print("Gemini: ", end="")
        for chunk in response:
            print(chunk.text, end="")
        print("\n")
    except Exception as e:
        print(f"Gemini encountered an error: {e}")
        print("\n")
        

