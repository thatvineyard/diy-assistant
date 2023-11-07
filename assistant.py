import argparse
import os
from pathlib import Path
from dotenv import load_dotenv
from colorama import Fore, Style

from components.assistance import Assistance
from components.chat import ChatSession
from components.azuretts import TextToSpeech
from components.chatparsers.multiplevoicesparser import parse
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

arg_parser = argparse.ArgumentParser(
  prog="diy-assistant 🤖",
  description="Talk to your own assistant!"
)
arg_parser.add_argument("-f", "--history_file", help="Path to previous history file to continue conversation", required=False)
args = arg_parser.parse_args()

history_file_name = None
if args.history_file is not None:
  history_file_path = Path(args.history_file)
  history_file_name = history_file_path.relative_to(HISTORY_DIRECTORY)

chatSession = ChatSession(OPENAI_KEY, HISTORY_DIRECTORY, history_file_name)
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
