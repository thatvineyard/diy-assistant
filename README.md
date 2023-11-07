# diy-assistant

In this workshop we will create our own AI powered assistant using OpenAI and make it do more for us than just our homework.

By leveraging OpenAIs ability to follow instructions we can turn the text it returns into meaningful syntax that we can parse and act on.

## Inspiration

The main inspiration for this workshop comes from the Twitch streamer and Youtube DougDoug who has been using AI and TTS to create challenges and games for himself. For example he recently played [Chess against an AI by having it explain what moves to make](https://youtu.be/l_wOsSda3Us?t=408). While in this case the moves are being executed by Doug, the use of chess notation made me wonder if there was a way to actually make it move the pieces by itself.

## Goal

1. Build a python script that communicates with OpenAI
2. Connect to Azure's text-to-speech to have the AI read its answers aloud.
3. Add instructions to the system prompt to make the AI include syntax that we can parse, and use this to affect the text-to-speech voice.
4. Add more instructions to allow it to search for Spotify songs.

## Prerequisites

- Python installed
- OpenAI Key [Can be found on your OpenAPI account page](https://platform.openai.com/account/api-keys) (will be provided at the workshop)
- Azure Speech Key [Can be found in Azure AI services > Speech service](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices) (will be provided at the workshop)
- Spotify Developer App [Can be found in your app that can be found on Spotify Dev dashboard](https://developer.spotify.com/dashboard) (will be provided at the workshop)

## Workshop format

There are branches for each goal that adds more instructions and helper files. Either checkout the branch and use the files there or merge them into your branch to get access to the files.

The branches are:

- `1-openai`
- `2-tts`
- `3-parse`
- `4-spotify`
