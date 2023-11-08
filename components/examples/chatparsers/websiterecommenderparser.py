import json
import webbrowser

from components.assistance import Assistance
from components.utils.voice.texttospeech import TextToSpeech
from components.utils.voice.azurevoices import Styles, Voices
from components.utils.voice.ttsscript import TtsScript

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:

  assistance = Assistance()
  
  try:
    response = json.loads(text)
  except json.JSONDecodeError:
    print("JSON structure not provided. Falling back on simple text-to-speech.")
    assistance.addAction(lambda: textToSpeech.speakText(text), "🗣️ Speaking response")
    return assistance

  if response['message'] is None:
    print("'message' key missing from JSON. Falling back on simple text-to-speech.")
    assistance.addAction(lambda: textToSpeech.speakText(text), "🗣️ Speaking response")
    return assistance
  
  assistance.addAction(lambda : print(response['message']), "🖨️ Printing message")
    
  script = TtsScript()
  script.addLine(response['message'], Voices.NANCY, Styles.excited, styleDegree=2, rate=1.6)
  assistance.addAction(lambda: textToSpeech.speakScript(script), "🗣️ Speaking message")
  
  if response['searchMethod'] is not None and response['searchTerm'] is not None:
    searchMethod, searchTerm = response['searchMethod'], response['searchTerm']
    searchUrl = getUrl(searchMethod, searchTerm)
    assistance.addAction(lambda : webbrowser.open_new(searchUrl), f'🔎 Opening browser and searching for {searchTerm} using {searchMethod}')
  
  return assistance

def getUrl(searchMethod: str, searchTerm: str):
  match searchMethod:
    case "images":
      return f'https://www.google.com/search?tbm=isch&q={searchTerm}'
    case "wikipedia":
      return f'https://www.wikipedia.org/w/index.php?search={searchTerm}'
    case "shopping":
      return f'https://www.amazon.se/s?k={searchTerm}'
    case "memes":
      return f'https://memes.com/search/?term={searchTerm}'
    case "youtube":
      return f'https://www.youtube.com/results?search_query={searchTerm}'
    case _:
      return f'https://www.google.com/search?tbm=isch&q={searchTerm}'

