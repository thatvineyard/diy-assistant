# STEP 2: TEXT-TO-SPEECH

## 1. Check out the new files

A new file `components/azuretts.py` has appeared and has been integrated with `assitant.py`. It is a class which exposes two functions: `speakText(self, text: str)` and `speakSSML(self, script: Script)`. There is also a file `components/script.py` which is a class to help build voice lines with different voices and emotions.

`speakText` is a simple version which reads the text in the default voice.

Try it out by running `py assistant.py` and listening to how it sounds.

## 2. Give your voice a voice

The second function `speakSSML` uses Speech Synthesis Markup to allow you to fine tune which voices and emotions should be used, allowing you to make changes within the text itself. You can read more about it on [Microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup).

When this is sent to Azure, the result will use the Jenny voice:

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        This is the text that is spoken.
    </voice>
</speak>
```

Using the `Script` class found in `components/script.py` you can decide how your voice should sound. There are also helped classes to let you pick the available voices and styles.

Create a `Script`, then call `addLine()` to build the script with the answer from your AI. Then replace `speakText` with `speakSSML` and it should use your new voice.

## Go to next step

Checkout branch `3-parse`.
