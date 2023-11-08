import json

from components.assistance import Assistance
from components.utils.voice.texttospeech import TextToSpeech
from components.utils.voice.azurevoices import Styles, Voices
from components.utils.voice.ttsscript import TtsScript

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:

  assistance = Assistance()
  
  try:
    lines = json.loads(text)
  except json.JSONDecodeError:
    print("Error parsing JSON. Falling back on simple text-to-speech.")
    assistance.addAction(lambda: textToSpeech.speakText(text), "Reading text")
    return assistance

  script = TtsScript()

  for line in lines:
    character = line['voice']
    text = line['text']
    emotion = line['emotion']
    
    voice = mapCharacterToVoice(character)
    style = mapEmotionToStyle(emotion)
    print_prefix = f'{character}: '
    
    script.addLine(text, voice=voice, style=style, styleDegree=2, rate=1.5, print_prefix=print_prefix)

  assistance.addAction(lambda : print(script.toString()), "Printing script")
  assistance.addAction(lambda : textToSpeech.speakScript(script), "Reading script")

  return assistance

def mapCharacterToVoice(character: str):
  match character:
    case "Aria":
      return Voices.ARIA
    case "Guy":
      return Voices.GUY
    case "Jason":
      return Voices.JASON
    case "Tony":
      return Voices.TONY
    case "Sara":
      return Voices.SARA
    case "Nancy":
      return Voices.NANCY
    case "Jane":
      return Voices.JANE
    case "Jenny":
      return Voices.JENNY
    case _:
      return Voices.ROBOT

def mapEmotionToStyle(emotion: str):
  match emotion:
    case "Sad":
      return Styles.sad
    case "Angry":
      return Styles.angry
    case "Happy":
      return Styles.cheerful
    case "Terrified":
      return Styles.terrified
    case "Shouting":
      return Styles.shouting
    case "Whispering":
      return Styles.whispering
    case "Excited":
      return Styles.excited
    case "Normal":
      return ""
    case _:
      return ""