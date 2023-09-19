import os
from dotenv import load_dotenv

from components.assistance import Assistance

# SETUP

load_dotenv(".env")
OPENAI_KEY=os.environ["OPENAI_KEY"]
AZURE_KEY_1=os.environ["AZURE_KEY_1"]
AZURE_SERVICE_REGION=os.environ["AZURE_SERVICE_REGION"]
SPOTIFY_APP_ID=os.environ["SPOTIFY_APP_ID"]
SPOTIFY_APP_SECRET=os.environ["SPOTIFY_APP_SECRET"]

# CHAT

# PARSE

assistance = Assistance()
assistance.addAction(lambda : print("Hello World"), "Print message")

# EXECUTE

assistance.execute()
