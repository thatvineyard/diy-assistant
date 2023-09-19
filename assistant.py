import os
from dotenv import load_dotenv
from datetime import date, datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


from components.chat import ChatSession
from components.voices import azuretts
from components.chatparsers import multiplevoicesparser, emotionparser, spotifyparser

load_dotenv(".env")
OPENAI_KEY=os.environ["OPENAI_KEY"]
AZURE_KEY_1=os.environ["AZURE_KEY_1"]
AZURE_SERVICE_REGION=os.environ["AZURE_SERVICE_REGION"]
SPOTIFY_APP_ID=os.environ["SPOTIFY_APP_ID"]
SPOTIFY_APP_SECRET=os.environ["SPOTIFY_APP_SECRET"]

chatSession = ChatSession(OPENAI_KEY)
textToSpeech = azuretts.TextToSpeech(AZURE_KEY_1, AZURE_SERVICE_REGION)
spotipy = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_APP_ID, client_secret=SPOTIFY_APP_SECRET))

# Receives a text from console input.
print("Ask your question")
question = input()

# ask openAi for an answer
answer = chatSession.chat(question)

print(answer)

assistance = spotifyparser.parse(answer, textToSpeech, spotipy)

assistance.execute()