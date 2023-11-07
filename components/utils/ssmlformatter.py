class SsmlFormatter:
  
    @staticmethod
    def encaseInSSMLTag(text: str):
      prefix = '''
      <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
        xmlns:mstts="https://www.w3.org/2001/mstts" 
        xml:lang="en-US"
      >
      '''
      postfix = '</speak>'
      return prefix + text + postfix
    
    @staticmethod
    def encaseInVoiceTag(text: str, voice: str):
      prefix = f'<voice name="{voice}">'
      postfix = '</voice>'
      return prefix + text + postfix

    @staticmethod
    def encaseInSpeakingStyleTag(text: str, style: str, styleDegree: float = 1):
        if styleDegree < 0.01:
          print("Style degree too low, clamping to 0.01")
          styleDegree = 0.01
        if styleDegree > 2:
          print("Style degree too high, clamping to 2")
          styleDegree = 2
        
        prefix = f'<mstts:express-as style="{style}" styledegree="{styleDegree}">'
        postfix = "</mstts:express-as>"

        return prefix + text + postfix
  
    @staticmethod
    def encaseInRateTag(text: str, rate: float):
        if rate < 0.5:
          print("Rate too low, clamping to 0.5")
          rate = 0.5
        if rate > 2:
          print("Rate too high, clamping to 2")
          rate = 2
        
        prefix = f'<prosody rate="{rate}">'
        postfix = "</prosody>"

        return prefix + text + postfix
