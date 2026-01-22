# Gemini CLI Chatbot

A command-line chatbot powered by **Google’s Gemini 2.5 Flash** model.  
This project demonstrates how to integrate Google’s Generative AI API into a Python application using environment variables for secure API key management.

---

## Features

- Interactive command-line chat with Gemini 2.5 Flash  
- Streaming AI responses in real-time  
- Secure API key loading using `.env` file  
- Input validation for empty messages  
- Graceful exit handling  

---

## Technologies Used

- Python  
- Google Generative AI (Gemini API)  
- python-dotenv  
- Environment variable management  

---

## How It Works

- Loads the API key from a `.env` file  
- Configures the Google Generative AI client  
- Creates a Gemini 2.5 Flash model instance  
- Starts a persistent chat session  
- Continuously:
  - Reads user input  
  - Sends it to Gemini  
  - Streams and prints the response  

---

## Requirements

- Python 3.9+  
- A Google Generative AI API key  

---

## Installation & Setup

### 1) Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

---

### 2) Install dependencies

pip install google-generativeai python-dotenv

---

### 3) Create a `.env` file

In the project root, create a file named:

.env

Inside it, add:

GOOGLE_API_KEY=your_api_key_here

*(Never push your `.env` file to GitHub)*

---

### 4) Run the chatbot

python chatbot.py

---

## Usage

Once running:

Say Hello to Gemini-2.5-Flash! Type 'exit' to end the chat.
You: Hello!
Gemini: Hello! How can I help you today?

Type `exit` to end the session.

---

## Project Structure

chatbot.py // Main chatbot script
.env // API key (not committed)
README.md // Documentation

---

## Error Handling

- Warns if API key is missing  
- Prevents sending empty messages  
- Catches and displays API errors gracefully  

---

## Future Improvements

- Add conversation history saving  
- Support system prompts  
- GUI version using Tkinter or web frontend  
- Multiple model selection  
