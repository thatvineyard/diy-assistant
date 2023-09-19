import re
from types import NoneType
from components.assistance import Assistance
from components.voices.azuretts import Script, TextToSpeech, Voices, Styles
from spotipy import Spotify

REGEX_STRING_WITH_NO_SQUARE_BRACKET = "[^\[\]]"

def parse(text: str, textToSpeech: TextToSpeech, spotipy: Spotify) -> Assistance:
  lines: re.Match = re.split(f'(\[{REGEX_STRING_WITH_NO_SQUARE_BRACKET}*\])', text, flags=re.MULTILINE)
  
  if isinstance(lines, NoneType):
    print("No match")
    return 
  
  script = Script()
  
  for line in lines:
    bracketWord = re.match(f'\[({REGEX_STRING_WITH_NO_SQUARE_BRACKET}*)\]', line)
    if(not isinstance(bracketWord, NoneType)):
      results = spotipy.search(bracketWord.group(1), 1)
      track = results['tracks']['items'][0]
      line = track["name"]
      
    script.addLine(line)
    

  assistance = Assistance()
  assistance.addAction(lambda : textToSpeech.speakSSML(script), "Reading script")
  if(track != None):
    assistance.addAction(lambda : print("🎵 This is where it would play a song if I had time to implement it properly 🎵"), f'Playing track: {track["name"]}')

  return assistance


