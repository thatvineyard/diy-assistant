import re
from types import NoneType
from components.assistance import Assistance
from components.azuretts import Script, TextToSpeech
from components.script import Voices, Styles

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

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:
  # Find lines that start with something in brackets and capture until
  # it reaches another square bracket. 
  # Eg. [foo] bar baz
  # It will group two groups:
  #   1. the bracketed word
  #   2. the line
  lines: re.Match = re.findall(f'^\[({REGEX_STRING_WITH_NO_SQUARE_BRACKET}*)\]({REGEX_STRING_WITH_NO_SQUARE_BRACKET}*)', text, flags=re.MULTILINE)
  
  if isinstance(lines, NoneType):
    print("No match")
    return 
  
  script = Script()
  
  # loop through each line
  for line in lines:
    character = line[0] # eg. "foo"
    text = line[1] # eg. bar baz
    
    # convert the character text to an Azure voice
    voice=mapCharacterToVoice(character)
    
    # add this line with the given voice
    script.addLine(text, voice=voice, styleDegree=2, rate=1.5)

  assistance = Assistance()
  assistance.addAction(lambda : textToSpeech.speakSSML(script), "Reading script")

  return assistance


