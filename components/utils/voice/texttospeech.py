import azure.cognitiveservices.speech as speechsdk

from components.utils.voice.ttsscript import TtsLine, TtsScript

# STEP 2

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

    def speakText(self, text: str):
        """Basic tts without directives, uses default voice."""
        
        result = self.speech_synthesizer.speak_text_async(text).get()
         
        TextToSpeech.__checkResult(result);

    def speakScript(self, script: TtsScript):
        """Collection of advanced tts using SSML syntax."""
        
        ssmlText = script.toSSML()
        result = self.speech_synthesizer.speak_ssml_async(ssmlText).get()

        TextToSpeech.__checkResult(result);

    def __checkResult(result):
        """Checks result of TTS generation and gives helpful error messages if something failed"""
        
        if result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print(
                        "Error details: {}".format(cancellation_details.error_details)
                    )
            print("Did you update the subscription info?")
