
class Voices:
  ARIA = "en-US-AriaNeural"
  GUY = "en-US-GuyNeural"
  JASON = "en-US-JasonNeural"
  TONY = "en-US-TonyNeural"
  SARA = "en-US-SaraNeural"
  NANCY = "en-US-NancyNeural"
  JANE = "en-US-JaneNeural"
  JENNY = "en-US-JennyNeural"

class Styles: 
    angry = "angry" # 	Expresses an angry and annoyed tone.
    chat = "chat" # 	Expresses a casual and relaxed tone.
    cheerful = "cheerful" # 	Expresses a positive and happy tone.
    customerservice = "customerservice" # 	Expresses a friendly and helpful tone for customer support.
    excited = "excited" # 	Expresses an upbeat and hopeful tone. It sounds like something great is happening and the speaker is happy about it.
    friendly = "friendly" # 	Expresses a pleasant, inviting, and warm tone. It sounds sincere and caring.
    hopeful = "hopeful" # 	Expresses a warm and yearning tone. It sounds like something good will happen to the speaker.
    sad = "sad" # 	Expresses a sorrowful tone.
    shouting = "shouting" # 	Expresses a tone that sounds as if the voice is distant or in another location and making an effort to be clearly heard.
    whispering = "whispering" # 	Expresses a soft tone that's trying to make a quiet and gentle sound.
    terrified = "terrified" # 	Expresses a scared tone, with a faster pace and a shakier voice. It sounds like the speaker is in an unsteady and frantic status.
    unfriendly = "unfriendly" # 	Expresses a cold and indifferent tone.

class Script:
    def __init__(self, defaultVoice: str = "en-US-AriaNeural"):
        self.lines = []
        self.defaultVoice = defaultVoice
    
    # Use this function to add a line to the script
    def addLine(self, text: str, voice: str = "", style: str = "", styleDegree: int = 1, rate: int = -1):
      if(style != ""):
          text = self.__encaseInSpeakingStyle(text, style, styleDegree)
      if(rate != -1):
          text = self.__encaseInRate(text, rate)
      if(voice == "" or voice == None):
        voice = self.defaultVoice
      text = self.__encaseInVoice(text, voice)
      
      self.lines.append(text)
      
    def getSSML(self):      
      allLines = "\n".join(self.lines)
      
      return self.__encaseInSSML(allLines)

    def __encaseInSSML(self, text: str):
      prefix = '''
      <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
        xmlns:mstts="https://www.w3.org/2001/mstts" 
        xml:lang="en-US"
      >
      '''
      postfix = '</speak>'
      return prefix + text + postfix

    def __encaseInVoice(self, text: str, voice: str):
      prefix = f'<voice name="{voice}">'
      postfix = '</voice>'
      return prefix + text + postfix

    def __encaseInSpeakingStyle(self, text: str, style: str, styleDegree: int = 1):
        if styleDegree < 0.01:
          print("Style degree too low, clamping to 0.01")
          styleDegree = 0.01
        if styleDegree > 2:
          print("Style degree too high, clamping to 2")
          styleDegree = 2
        
        prefix = f'<mstts:express-as style="{style}" styledegree="{styleDegree}">'
        postfix = "</mstts:express-as>"

        return prefix + text + postfix
  
    def __encaseInRate(self, text: str, rate: int):
        if rate < 0.5:
          print("Rate too low, clamping to 0.5")
          rate = 0.5
        if rate > 2:
          print("Rate too high, clamping to 2")
          rate = 2
        
        prefix = f'<prosody rate="{rate}">'
        postfix = "</prosody>"

        return prefix + text + postfix
