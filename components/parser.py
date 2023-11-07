from components.assistance import Assistance
from components.azuretts import TextToSpeech
from components.script import Script


def parse(text: str, textToSpeech: TextToSpeech) -> Assistance:
  # Do some sort of string matching, such as a regex.
  # Act on what you find. Maybe something can be mapped to a certain voice, style or rate of speech?
  # Build a script using `addLine()` with different parameters.
  
  script = Script()
  
  script.addLine(text) # Replace this with your logic based on the text
  
  assistance = Assistance()
  assistance.addAction(lambda : print(text), "Print message")
  assistance.addAction(lambda : textToSpeech.speakSSML(script), "Reading message")
  
  # Feel free to have the AI do other things than just affect the way the text is read. This will come up in the next step.
  
  return assistance