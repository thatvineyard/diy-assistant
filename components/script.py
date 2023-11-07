
from components.utils.ssmlformatter import SsmlFormatter

class Voices:
  ARIA = "en-US-AriaNeural"
  GUY = "en-US-GuyNeural"
  JASON = "en-US-JasonNeural"
  TONY = "en-US-TonyNeural"
  SARA = "en-US-SaraNeural"
  NANCY = "en-US-NancyNeural"
  JANE = "en-US-JaneNeural"
  JENNY = "en-US-JennyNeural"
  ROBOT = "en-US-AIGenerate1Neural"

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

class Line:
  def __init__(self, text: str, voice: str, style: str = "", styleDegree: int = 1, rate: int = -1):
    self.text = text
    self.voice = voice
    self.style = style
    self.styleDegree = styleDegree
    self.rate = rate
  
  def toSSML(self):
    ssml_text = self.text
    if(self.style != ""):
        ssml_text = SsmlFormatter.encaseInSpeakingStyleTag(ssml_text, self.style, self.styleDegree)
    if(self.rate != -1):
        ssml_text = SsmlFormatter.encaseInRateTag(ssml_text, self.rate)
    ssml_text = SsmlFormatter.encaseInVoiceTag(ssml_text, self.voice)
        
    return ssml_text

class Script:
    def __init__(self, defaultVoice: str = "en-US-AriaNeural"):
        self.lines: list[Line] = []
        self.defaultVoice = defaultVoice
    
    # Use this function to add a line to the script
    def addLine(self, text: str, voice: str = "", style: str = "", styleDegree: int = 1, rate: int = -1):
      if(voice == ""):
        voice = self.defaultVoice
      
      self.lines.append(Line(text, voice, style, styleDegree, rate))
      
    def getSSML(self):      
      allLines = "\n".join(map(lambda line: line.toSSML(), self.lines))
      allLines = SsmlFormatter.encaseInSSMLTag(allLines)
      return allLines

    def toString(self):
      result = ""
      for line in self.lines:
        result += f'{line.voice}:  {line.text}\n'
      return result