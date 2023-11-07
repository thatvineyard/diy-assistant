import os
from dotenv import load_dotenv
from colorama import Fore, Style

from components.assistance import Assistance
from components.chat import ChatSession
from components.azuretts import TextToSpeech
from components.parser import parse
from components.script import Script, Voices, Styles
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# SETUP

load_dotenv(".env")
OPENAI_KEY=os.environ["OPENAI_KEY"]
AZURE_KEY_1=os.environ["AZURE_KEY_1"]
AZURE_SERVICE_REGION=os.environ["AZURE_SERVICE_REGION"]
SPOTIFY_APP_ID=os.environ["SPOTIFY_APP_ID"]
SPOTIFY_APP_SECRET=os.environ["SPOTIFY_APP_SECRET"]
HISTORY_DIRECTORY=os.environ["HISTORY_DIRECTORY"]

chatSession = ChatSession(OPENAI_KEY, HISTORY_DIRECTORY)
textToSpeech = TextToSpeech(AZURE_KEY_1, AZURE_SERVICE_REGION)
spotipy = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_APP_ID, client_secret=SPOTIFY_APP_SECRET))

# CHAT

while True: 
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
