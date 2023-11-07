import json
import re
from types import NoneType
from components.assistance import Assistance
from components.texttospeech import TextToSpeech
from components.utils.azurevoices import Voices
from components.utils.ttsscript import TtsScript

REGEX_STRING_WITH_NO_SQUARE_BRACKET = "[^\[\]]"

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

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:

  assistance = Assistance()
  
  try:
    lines = json.loads(text)
  except json.JSONDecodeError:
    assistance.addAction(lambda: textToSpeech.speakText("There was an unexpected error when parsing JSON"), "Handling error")
    return assistance

  script = TtsScript()

  for line in lines:
    character = line['voice']
    text = line['text']
    emotion = line['emotion']
    script.addLine(text, voice=mapCharacterToVoice(character), styleDegree=2, rate=1.5)

  assistance.addAction(lambda : print(script.toString()), "Printing script")
  assistance.addAction(lambda : textToSpeech.speakSSML(script), "Reading script")

  return assistance


