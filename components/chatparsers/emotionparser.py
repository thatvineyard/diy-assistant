import re
from types import NoneType
from components.assistance import Assistance
from components.azuretts import Script, TextToSpeech, Voices, Styles

REGEX_STRING_WITH_NO_SQUARE_BRACKET = "[^\[\]]"

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
    case "Normal", _:
      return ""
    

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:
  lines: re.Match = re.findall(f'\[({REGEX_STRING_WITH_NO_SQUARE_BRACKET}*)\]({REGEX_STRING_WITH_NO_SQUARE_BRACKET}*)', text, flags=re.MULTILINE)
  
  if isinstance(lines, NoneType):
    print("No match")
    return 
  
  script = Script()
  
  for line in lines:
    emotion = line[0]
    text = line[1]
    
    script.addLine(text, voice=Voices.GUY, style=mapEmotionToStyle(emotion), styleDegree=2, rate=1.5)

  assistance = Assistance()
  assistance.addAction(lambda : textToSpeech.speakSSML(script), "Reading script")

  return assistance
