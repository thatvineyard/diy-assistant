import json

from components.assistance import Assistance
from components.utils.voice.texttospeech import TextToSpeech
from components.utils.voice.azurevoices import Styles, Voices
from components.utils.voice.ttsscript import TtsScript

# STEP 3

def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:

  assistance = Assistance()
    
  # Try to load the json. This will fail if the assistant decides to answer in a non-JSON way, 
  # which it will do a lot. 
  try:
    lines = json.loads(text)
  except json.JSONDecodeError:
    print("JSON structure not provided. Falling back on simple text-to-speech.")
    assistance.addAction(lambda : print(text), "🖨️ Printing response")
    assistance.addAction(lambda: textToSpeech.speakText(text), "🗣️ Speaking response")
    return assistance

  script = TtsScript()

  # If we only got one line for some reason, put it in a list
  if isinstance(lines, dict):
    lines = [lines]

  # Go through each line given in the response and add a line to the TTS script
  for line in lines:
    character = line['voice']
    text = line['text']
    emotion = line['emotion']
    
    voice = mapCharacterToVoice(character)
    style = mapEmotionToStyle(emotion)
    print_prefix = f'{character}: '
    
    script.addLine(text, voice=voice, style=style, styleDegree=2, rate=1.5, print_prefix=print_prefix)
  
  # Set up the actions in the assistance.
  assistance.addAction(lambda : print(script.toString()), "🖨️ Printing script")
  assistance.addAction(lambda: textToSpeech.speakScript(script), "🗣️ Speaking script")

  return assistance

def mapCharacterToVoice(character: str):
  """Switch function to get the correct voice"""
  
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
  """Switch function to get the correct style"""
  
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