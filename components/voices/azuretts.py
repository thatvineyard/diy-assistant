import azure.cognitiveservices.speech as speechsdk


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
    advertisement_upbeat = "advertisement_upbeat" # 	Expresses an excited and high-energy tone for promoting a product or service.
    affectionate = "affectionate" # 	Expresses a warm and affectionate tone, with higher pitch and vocal energy. The speaker is in a state of attracting the attention of the listener. The personality of the speaker is often endearing in nature.
    angry = "angry" # 	Expresses an angry and annoyed tone.
    assistant = "assistant" # 	Expresses a warm and relaxed tone for digital assistants.
    calm = "calm" # 	Expresses a cool, collected, and composed attitude when speaking. Tone, pitch, and prosody are more uniform compared to other types of speech.
    chat = "chat" # 	Expresses a casual and relaxed tone.
    cheerful = "cheerful" # 	Expresses a positive and happy tone.
    customerservice = "customerservice" # 	Expresses a friendly and helpful tone for customer support.
    depressed = "depressed" # 	Expresses a melancholic and despondent tone with lower pitch and energy.
    disgruntled = "disgruntled" # 	Expresses a disdainful and complaining tone. Speech of this emotion displays displeasure and contempt.
    documentary_narration = "documentary-narration" # 	Narrates documentaries in a relaxed, interested, and informative style suitable for dubbing documentaries, expert commentary, and similar content.
    embarrassed = "embarrassed" # 	Expresses an uncertain and hesitant tone when the speaker is feeling uncomfortable.
    empathetic = "empathetic" # 	Expresses a sense of caring and understanding.
    envious = "envious" # 	Expresses a tone of admiration when you desire something that someone else has.
    excited = "excited" # 	Expresses an upbeat and hopeful tone. It sounds like something great is happening and the speaker is happy about it.
    fearful = "fearful" # 	Expresses a scared and nervous tone, with higher pitch, higher vocal energy, and faster rate. The speaker is in a state of tension and unease.
    friendly = "friendly" # 	Expresses a pleasant, inviting, and warm tone. It sounds sincere and caring.
    gentle = "gentle" # 	Expresses a mild, polite, and pleasant tone, with lower pitch and vocal energy.
    hopeful = "hopeful" # 	Expresses a warm and yearning tone. It sounds like something good will happen to the speaker.
    lyrical = "lyrical" # 	Expresses emotions in a melodic and sentimental way.
    narration_professional = "narration-professional" # 	Expresses a professional, objective tone for content reading.
    narration_relaxed = "narration-relaxed" # 	Expresses a soothing and melodious tone for content reading.
    newscast = "newscast" # 	Expresses a formal and professional tone for narrating news.
    newscast_casual = "newscast-casual" # 	Expresses a versatile and casual tone for general news delivery.
    newscast_formal = "newscast-formal" # 	Expresses a formal, confident, and authoritative tone for news delivery.
    poetry_reading = "poetry-reading" # 	Expresses an emotional and rhythmic tone while reading a poem.
    sad = "sad" # 	Expresses a sorrowful tone.
    serious = "serious" # 	Expresses a strict and commanding tone. Speaker often sounds stiffer and much less relaxed with firm cadence.
    shouting = "shouting" # 	Expresses a tone that sounds as if the voice is distant or in another location and making an effort to be clearly heard.
    sports_commentary = "sports_commentary" # 	Expresses a relaxed and interested tone for broadcasting a sports event.
    sports_commentary_excited = "sports_commentary_excited" # 	Expresses an intensive and energetic tone for broadcasting exciting moments in a sports event.
    whispering = "whispering" # 	Expresses a soft tone that's trying to make a quiet and gentle sound.
    terrified = "terrified" # 	Expresses a scared tone, with a faster pace and a shakier voice. It sounds like the speaker is in an unsteady and frantic status.
    unfriendly = "unfriendly" # 	Expresses a cold and indifferent tone.

class Script:
    def __init__(self, defaultVoice: str = "en-US-AriaNeural"):
        self.lines = []
        self.defaultVoice = defaultVoice

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


class TextToSpeech:
    def __init__(self, speech_key, service_region, defaultVoice: str = "en-US-AriaNeural"):
        self.speech_key = speech_key
        self.service_region = service_region

        # Creates an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").
        speech_config = speechsdk.SpeechConfig(
            subscription=speech_key, region=service_region
        )

        # Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
        speech_config.speech_synthesis_voice_name = defaultVoice

        # Creates a speech synthesizer using the default speaker as audio output.
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config
        )

    # Basic tts without directives, uses default voice.
    def speakText(self, text: str):
        result = self.speech_synthesizer.speak_text_async(text).get()

        self.__checkResult(result);

    # More advanced tts using SSML syntax.    
    def speakSSML(self, script: Script, runAsync: bool = False):
        ssmlText = script.getSSML()
        if(runAsync):
          result = self.speech_synthesizer.speak_ssml_async(ssmlText).get()
        else:
          result = self.speech_synthesizer.speak_ssml(ssmlText)

        TextToSpeech.__checkResult(result);

    def __checkResult(result):
      # Checks result.
        if result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print(
                        "Error details: {}".format(cancellation_details.error_details)
                    )
            print("Did you update the subscription info?")
