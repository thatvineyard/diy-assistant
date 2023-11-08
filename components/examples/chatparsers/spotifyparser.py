import re

from components.assistance import Assistance
from components.utils.spotify.spotifyclient import SpotipyClient, Track
from components.utils.voice.texttospeech import TextToSpeech
from components.utils.voice.azurevoices import Styles, Voices
from components.utils.voice.ttsscript import TtsScript


REGEX_STRING_WITH_NO_SQUARE_BRACKET = "[^\[\]]"

def parse(text: str, textToSpeech: TextToSpeech, spotipy: SpotipyClient) -> Assistance:
  assistance = Assistance()
  
  # Using regex we try split up the text on the song recommendation, including the recommendation as well as what comes before and after.
  lines: re.Match = re.split(f'(\[{REGEX_STRING_WITH_NO_SQUARE_BRACKET}*\])', text, flags=re.MULTILINE)
  
  if lines is None:
    print("Could not find song recommendation in response. Falling back on simple text-to-speech.")
    assistance.addAction(lambda : print(text), "🖨️ Printing response")
    assistance.addAction(lambda: textToSpeech.speakText(text), "🗣️ Speaking response")
    return 
  
  # We will rebuild the text excluding the recommendation so it's not read out. 
  text = ""
  
  # Go through lines and if there is a song recommendation, search for it and save it
  track: Track = None
  for line in lines:
    bracketWord = re.match(f'\[({REGEX_STRING_WITH_NO_SQUARE_BRACKET}*)\]', line)
    
    if bracketWord is not None:
      searchTerm = bracketWord.group(1)
      track = spotipy.searchForTrack(searchTerm=searchTerm)
    else:
      text += line
  
  # If there is a track we want to play it quietly while the TTS talks
  if track is not None:
    assistance.addAction(lambda : spotipy.playTrack(track), f'▶️ Playing track: {track.name}')
    assistance.addAction(lambda: spotipy.setVolume(50), f'🔉 Setting volume to 50%')
  
  # Set up resonse in voice and console
  assistance.addAction(lambda : print(text), "🖨️ Printing response")
  script = TtsScript()
  script.addLine(text, Voices.JASON, Styles.sad, styleDegree=2, rate=1.2)
  assistance.addAction(lambda : textToSpeech.speakScript(script), "🗣️ Speaking answer")
  
  # After reading we crank the volume
  assistance.addAction(lambda: spotipy.setVolume(100), f'🔊 Setting volume to 100%')
    
  return assistance


