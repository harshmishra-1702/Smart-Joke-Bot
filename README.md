# 🤖 Smart Joke Bot

A simple Python-based "agent" that fetches random jokes from an external API and displays them through a friendly web interface.

## 🌟 Features
- **API Fetching:** Uses the `requests` library to get jokes from the Official Joke API.
- **Web UI:** Built with **Gradio**, allowing users to interact with the bot in a browser.
- **Environment Management:** Uses `python-dotenv` to keep configuration separate from the code.

## 🛠️ How to Setup & Run
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/harshmishra-1702/Smart-Joke-Bot.git](https://github.com/harshmishra-1702/Smart-Joke-Bot.git)
   ```
2. **Install the dependencies:**
   ```bash
    pip install -r requirements.txt
   ```
3.**Run the Bot:**
   ```bash
   python bot.py
   ```
4. **Setup Environment Variables:**
   Create a `.env` file in the project folder:
   ```text
   MY_SECRET_APP_NAME=JokeBot
   
