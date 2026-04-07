import requests
import json
import os
from dotenv import load_dotenv
import gradio as gr
'''harsh'''

load_dotenv()
app_name=os.getenv("MY_SECRET_APP_NAME")

class JokeAgent:
    def __init__(self,name):
        self.agent_name=name
        self.api_url="https://official-joke-api.appspot.com/random_joke"

    def fetch_joke(self):
        try:
            response=requests.get(self.api_url)
            data = response.json()

            setup = data["setup"]
            punchline = data["punchline"]

            return f"{self.agent_name} says: \n\n{setup}\n... {punchline}"
        except Exception as e:
            return f"Oops! {self.agent_name} broke. Error: {e}"
        

my_bot=JokeAgent(name=app_name)

interface = gr.Interface(
    fn=my_bot.fetch_joke,
    inputs=None,
    outputs="text",
    title="Smart Joke Bot",
    description="Click Generate to fetch the joke from the outside world!"
)

if __name__=="__main__":
    interface.launch()
