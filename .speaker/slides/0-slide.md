<!-- classes: talk -->

# diy-assistant 🤖

Carl Wingårdh, Andreas Röckert

## Build your own assistant using LLMs

---
<!-- classes: talk -->

## What can you use LLMs for?

<!-- block-start: grid -->

<!-- fragments-start -->

<!-- block-start: column -->

<!-- note If you're a student with 5 minutes to your deadline -->

```ascii
    ________________________________
   / A toilet is a piece of         \
  | sanitary hardware that collects  |
  |  human urine...                  |
🤖/\________________________________/
```

## ✍️

### Cheating on your homework

<!-- block-end -->

<!-- block-start: column -->

<!-- note Maybe you are a megacorporation hell bent on saving money wherever you can -->
```ascii
    _____________________________
   / Taylor Swift was seen today \
   | eating a hot dog. Hot dog   |
   | stock price surge ...       |
🤖/\____________________________/
```

## 🤖

### Fully automating writing articles and handling customer relations

<!-- block-end -->

<!-- block-start: column -->

<!-- note A shady amazon retailer who wants it to look like people like your product -->
```ascii

    _____________________________
   / I am really happy with the  \
   | purchase of my Bored Ape NFT | 
🤖/\_____________________________/
```

## 👍

### Automate comments that say good things

<!-- block-end -->

<!-- fragments-end -->

<!-- block-end -->

---

<!-- classes: talk -->

# It's alive! 🧌

It __almost__ seems like it is has intelligence and can make decisions

```ascii
    _______________________________________________________________
   / My favorite song is William Shatner's rendition of Rocket man \
🤖/\_______________________________________________________________/
```

But can we make it act on those "decisions"?

```ascii
> 🤖 Play Rocket Man cover by William Shatner in Rocket man 
```

That's what we want to do today.

---
<!-- classes: talk -->

# The plan 🤔

<!-- 1. Start chatting with OpenAI in a Python script
2. Connect to Azure's text-to-speech to have the AI read its answers aloud.
3. Add instructions to the system prompt to make the AI include syntax that we can parse, and use this to affect the text-to-speech voice.
4. Add more instructions to allow it to search for Spotify songs. -->

1. Start chatting with OpenAI in a Python script
2. Tell it how to respond to you
3. Give it a voice
4. Give it the power to do stuff

---
<!-- classes: talk -->
<!-- qr: https://join.slack.com/share/enQtNjE3NTMwNDcwNjY5My05NzE1Y2Y3OGU3MTdlMjBkMDBhZjg5MmY3Yjk2NWU3MGNmNzQwOTNhOWEyOTQ0ZDExNTFlOTdmNTY4Y2E2OTdj -->
# #opkoko-diyassistant

- Link to repo
- Api-keys (will be rotated after the workshop)
- Board for workshop events

<!-- <https://github.com/thatvineyard/diy-assistant> -->

---
<!-- classes: talk -->
# Workshop format

Work from branches in the repo.

- `0-setup`
- `1-openai`
- `2-tts`
- `3-parse`
- `4-spotify`

---
<!-- classes: talk -->
# Step-0: Setup

Setup virtual environment (venv)

```bash
python -m venv .venv
```

1. Activate venv

```pwsh
./.venv/Scripts/activate
```

```bash
source .venv/Scripts/activate
```

```zsh
source .venv/bin/active
```

2. Install pacakges

```bash
python install -r requirements.txt
```

3. Test run the application, and submit the weeks time sheet!

```bash
python diy-assistant.py
```

4. Add an action to `diy-assistant.py`

<!-- Make sure to give an overview of the code and that we have abstracted execution by the assistant to actions -->

---
<!-- classes: talk -->
# Step-1: Open AI

- System prompts are sent alongside message.
- Decide personality and behavior of AI.
- Best way to get it to stop being so clean, friendly and corporate.

Try making your own personality!

```bash
git checkout 1-openai
```

New files:

```bash
components/chat.py

components/system-prompt.txt
```

---

# Step-1: Open AI - retro
<!-- classes: talk -->
What did you think?

Post promts in #opkoko-diyassistant

---
<!-- classes: talk -->
# Step-2: Text to Speach

Give your bot a voice!

New files in `components/azuretts.py`

Try new actions `speakText(text)` and `speakSSML(script)`.

---
<!-- classes: talk -->
# Step-3: Parser

Instruct OpenAI to provide text based instructions in a specific syntax, e.g. json.

---
<!-- classes: talk -->
# Step-4: Spotify

- Parse the output to another api-call.
- In this case, make it play music with spotify.
- If you want to participate, name and email registered to spotify account in #opkoko-diyassistant

---
<!-- classes: talk -->
# Recap

Code ❤️ OpenAI

Leverage creativity of LLM and provide it with natural language instructions which can be parsed using python code.

1. Communicate with OpenAI
2. Give the assistant a voice
3. Parse text based instructions in specific syntax
4. Parse to additional api-calls, spotify

---
<!-- classes: talk -->
# Thanks

Bow down to your future overlord 🤖