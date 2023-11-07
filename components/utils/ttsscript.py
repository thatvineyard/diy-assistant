
from components.utils.ssmlformatter import SsmlFormatter

class TtsLine:
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

class TtsScript:
    def __init__(self, defaultVoice: str = "en-US-AriaNeural"):
        self.lines: list[TtsLine] = []
        self.defaultVoice = defaultVoice
    
    # Use this function to add a line to the script
    def addLine(self, text: str, voice: str = "", style: str = "", styleDegree: int = 1, rate: int = -1):
      if(voice == ""):
        voice = self.defaultVoice
      
      self.lines.append(TtsLine(text, voice, style, styleDegree, rate))
      
    def toSSML(self):      
      allLines = "\n".join(map(lambda line: line.toSSML(), self.lines))
      allLines = SsmlFormatter.encaseInSSMLTag(allLines)
      return allLines

    def toString(self):
      result = ""
      for line in self.lines:
        result += f'{line.voice}:  {line.text}\n'
      return result