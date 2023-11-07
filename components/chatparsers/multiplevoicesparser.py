import json
import re
from types import NoneType
from components.assistance import Assistance
from components.voices.azuretts import Script, TextToSpeech, Voices, Styles

REGEX_STRING_WITH_NO_SQUARE_BRACKET = "[^\[\]]"

def mapCharacterToVoice(character: str):
  match character:
    case "Aria", _:
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
    case "Robot":
      return Voices.ROBOT

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:
  lines = json.loads(text)
  
  script = Script()

  for line in lines:
    character = line['voice']
    text = line['text']
    emotion = line['emotion']
    
    script.addLine(text, voice=mapCharacterToVoice(character), styleDegree=2, rate=1.5)

  assistance = Assistance()
  assistance.addAction(lambda : textToSpeech.speakSSML(script), "Reading script")

  return assistance


