import re

from components.assistance import Assistance
from components.utils.spotify.spotifyclient import SpotipyClient, Track
from components.utils.voice.texttospeech import TextToSpeech
from components.utils.voice.azurevoices import Styles, Voices
from components.utils.voice.ttsscript import TtsScript


REGEX_STRING_WITH_NO_SQUARE_BRACKET = "[^\[\]]"

def parse(text: str, textToSpeech: TextToSpeech, spotipy: SpotipyClient) -> Assistance:
  assistance = Assistance()
  
  lines: re.Match = re.split(f'(\[{REGEX_STRING_WITH_NO_SQUARE_BRACKET}*\])', text, flags=re.MULTILINE)
  
  if lines is None:
    assistance.addAction(lambda : textToSpeech.speakText(text), "Could not find a song in answer, reading answer")
    return 
  
  response = ""
  track: Track = None
  
  for line in lines:
    bracketWord = re.match(f'\[({REGEX_STRING_WITH_NO_SQUARE_BRACKET}*)\]', line)
    
    if bracketWord is not None:
      searchTerm = bracketWord.group(1)
      track = spotipy.searchForTrack(searchTerm=searchTerm)
      line = track.name
    
    response += line
    
  if track is not None:
    assistance.addAction(lambda : spotipy.playTrack(track), f'Playing track: {track.name}')
  
  assistance.addAction(lambda: spotipy.setVolume(20), f'Setting volume to 20%')
  
  script = TtsScript()
  script.addLine(response, Voices.JASON, Styles.sad, styleDegree=2, rate=1.2)
  assistance.addAction(lambda : textToSpeech.speakLine(script), "Speaking answer")
  
  assistance.addAction(lambda: spotipy.setVolume(100), f'Setting volume to 100%')
    
  return assistance


