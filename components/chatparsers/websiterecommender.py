import json
from components.assistance import Assistance
from components.texttospeech import TextToSpeech
import webbrowser

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:

  assistance = Assistance()
  
  try:
    response = json.loads(text)
  except json.JSONDecodeError:
    print("Error parsing JSON. Falling back on simple text-to-speech.")
    assistance.addAction(lambda: textToSpeech.speakText(text), "Reading text")
    return assistance

  if response['message'] is None:
    print("'message' key missing from JSON. Falling back on simple text-to-speech.")
    assistance.addAction(lambda: textToSpeech.speakText(text), "Reading text")
    return assistance
  
  assistance.addAction(lambda : print(response['message']), "Printing script")
  assistance.addAction(lambda: textToSpeech.speakText(response['message']), "Reading text")
  
  if response['searchMethod'] is None or response['searchTerm'] is None:
    return assistance
  
  searchUrl = getUrl(response['searchMethod'], response['searchTerm'])
  
  assistance.addAction(lambda : webbrowser.open_new(searchUrl), "Printing script")
  
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
    case _:
      return f'https://www.google.com/search?tbm=isch&q={searchTerm}'

