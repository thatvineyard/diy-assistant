import os
from dotenv import load_dotenv
from colorama import Fore, Style

from components.assistance import Assistance
from components.chat import ChatSession
from components.azuretts import TextToSpeech
from components.parser import parse
from components.script import Script, Voices, Styles

# SETUP

load_dotenv(".env")
OPENAI_KEY=os.environ["OPENAI_KEY"]
AZURE_KEY_1=os.environ["AZURE_KEY_1"]
AZURE_SERVICE_REGION=os.environ["AZURE_SERVICE_REGION"]
SPOTIFY_APP_ID=os.environ["SPOTIFY_APP_ID"]
SPOTIFY_APP_SECRET=os.environ["SPOTIFY_APP_SECRET"]

chatSession = ChatSession(OPENAI_KEY)
textToSpeech = TextToSpeech(AZURE_KEY_1, AZURE_SERVICE_REGION)

# CHAT

# Receives a text from console input.
question = input(f'{Fore.GREEN}INPUT: {Style.RESET_ALL}')


# ask openAi for an answer
answer = chatSession.chat(question)

# print answer to debug if needed
# print(f'{Fore.LIGHTMAGENTA_EX}RESPONSE:\n{Style.RESET_ALL} {answer}')

# PARSE

assistance = parse(answer, textToSpeech)

# EXECUTE

assistance.execute()
