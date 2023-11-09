import argparse
import os
from pathlib import Path
from dotenv import load_dotenv
import webbrowser

from components.assistance import Assistance

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

############
### CHAT ###
############

assistance = Assistance()
assistance.addAction(lambda : webbrowser.open("https://me73379-iaccess.deltekfirst.com/oauth"), "Opening maconomy")
assistance.execute()
