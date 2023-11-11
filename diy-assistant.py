import argparse
import os
from pathlib import Path
from dotenv import load_dotenv
from colorama import Fore, Style
import webbrowser

from components.assistance import Assistance
from components.chat import ChatSession
from components.examples.chatparsers.multiplevoicesparser import parse
from components.utils.voice.texttospeech import TextToSpeech
from components.utils.spotify.spotifyclient import SpotipyClient

##############
### SET UP ###
##############

# Read environment
load_dotenv(".env")
OPENAI_KEY=os.environ["OPENAI_KEY"]
AZURE_KEY_1=os.environ["AZURE_KEY_1"]
AZURE_SERVICE_REGION=os.environ["AZURE_SERVICE_REGION"]
SPOTIFY_CLIENT_ID=os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET=os.environ["SPOTIFY_CLIENT_SECRET"]
HISTORY_DIRECTORY=os.environ["HISTORY_DIRECTORY"]

# Set up argument parsing
arg_parser = argparse.ArgumentParser(
  prog="diy-assistant 🤖",
  description="Talk to your own assistant!"
)
arg_parser.add_argument("-f", "--history_file", help=f'If a history file exists, it will be loaded to continue conversation, otherwise it will be the filename given to the new history file. NOTE: Needs to be in the history_directory ({HISTORY_DIRECTORY})', required=False)
args = arg_parser.parse_args()

# Set up utilities
# STEP 1: 
chatSession = ChatSession(OPENAI_KEY, HISTORY_DIRECTORY, args.history_file)
# STEP 2: 
textToSpeech = TextToSpeech(AZURE_KEY_1, AZURE_SERVICE_REGION)
# STEP 4: 
spotipy = SpotipyClient(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)

############
### CHAT ###
############

while True: 
  # STEP 1: Receives a text from console input.
  question: str = input(f'{Fore.GREEN}INPUT: {Style.RESET_ALL}')

  # STEP 1: ask openAI for an answer
  answer: str = chatSession.chat(question)

  # print answer to debug if needed
  # print(f'{Fore.LIGHTMAGENTA_EX}RESPONSE:\n{Style.RESET_ALL} {answer}')

  # STEP 0: Basic assistance
  # assistance = Assistance()
  # assistance.addAction(lambda : webbrowser.open("https://me73379-iaccess.deltekfirst.com/oauth"), "Print message")
  # assistance.execute()

  # STEP 2: Text-to-speech assistance
  # assistance = Assistance()
  # assistance.addAction(lambda : print(text), "Print message")
  # assistance.addAction(lambda : textToSpeech.speakText(text), "Print message")
  # assistance.execute()

  # STEP 3: Extract parsing to it's own function
  assistance = parse(answer, textToSpeech)
  assistance.execute()
