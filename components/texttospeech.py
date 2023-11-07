import azure.cognitiveservices.speech as speechsdk

from components.utils.ttsscript import TtsScript


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
  angry = "angry"                     # Expresses an angry and annoyed tone.
  chat = "chat"                       # Expresses a casual and relaxed tone.
  cheerful = "cheerful"               # Expresses a positive and happy tone.
  customerservice = "customerservice" # Expresses a friendly and helpful tone for customer support.
  excited = "excited"                 # Expresses an upbeat and hopeful tone. It sounds like something great is happening and the speaker is happy about it.
  friendly = "friendly"               # Expresses a pleasant, inviting, and warm tone. It sounds sincere and caring.
  hopeful = "hopeful"                 # Expresses a warm and yearning tone. It sounds like something good will happen to the speaker.
  sad = "sad"                         # Expresses a sorrowful tone.
  shouting = "shouting"               # Expresses a tone that sounds as if the voice is distant or in another location and making an effort to be clearly heard.
  whispering = "whispering"           # Expresses a soft tone that's trying to make a quiet and gentle sound.
  terrified = "terrified"             # Expresses a scared tone, with a faster pace and a shakier voice. It sounds like the speaker is in an unsteady and frantic status.
  unfriendly = "unfriendly"           # Expresses a cold and indifferent tone.

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
         
        TextToSpeech.__checkResult(result);

    # More advanced tts using SSML syntax.    
    def speakSSML(self, script: TtsScript):
        ssmlText = script.getSSML()
        result = self.speech_synthesizer.speak_ssml_async(ssmlText).get()

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
