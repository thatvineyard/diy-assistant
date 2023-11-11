<!-- classes: talk -->

# diy-assistant workshop

# 🤖

Build your own assistant using LLMs and python

---
<!-- classes: talk -->

<!-- block-start: grid -->

<!-- block-start: column -->

## Carl Wingårdh
![Carl](https://cache.sessionize.com/image/0a15-400o400o2-L7D94sCGh6pgjQwZb4etgw.png)

Developer at Uppsalakontoret

<!-- block-end -->
<!-- block-start: column -->

## Andreas Röckert
![Andreas](https://cache.sessionize.com/image/68e0-400o400o2-EN4GZd1sXvbNTdU8ZUTaTA.png)

Developer at Uppsalakontoret

<!-- block-end -->

<!-- block-end -->

---
<!-- classes: talk -->

# A primer on large language models

---
<!-- classes: talk -->

## What can you use LLMs for?

<!-- block-start: grid -->

<!-- block-start: column -->

<!-- note If you're a student with 5 minutes to your deadline -->

```ascii

    ________________________
   / A toilet is a piece of \
  | sanitary hardware that   |
  | collects human urine...  |
🤖/\________________________/

```

## ✍️

#### Cheating on your homework

<!-- block-end -->

<!-- block-start: column -->

<!-- note Maybe you are a megacorporation hell bent on saving money wherever you can -->
```ascii
    ________________________
   / Taylor Swift was seen  \
   | today eating a hot dog. |
   | Hot dog stock price     |
   | surge ...               |
🤖/\________________________/

```

## 📰

#### Fully automating writing articles

<!-- block-end -->

<!-- block-start: column -->

<!-- note A shady amazon retailer who wants it to look like people like your product -->
```ascii

    ________________________
   / I am really happy with \
   | the purchase of my      |
   | Bored Ape NFT           | 
🤖/\________________________/

```

## 👍

#### Automate fake comments that say good things when nobody else seems to

<!-- block-end -->

<!-- block-end -->

---

<!-- classes: talk -->

![Frankenstein](https://i.giphy.com/media/tze1mGedykiuk/giphy.webp)

# It's alive!


It __almost__ seems like it is has intelligence and can make decisions

<!-- fragments-start -->
```ascii
    _______________________________________________________________
   / My favorite song is William Shatner's rendition of Rocket man \
🤖/\_______________________________________________________________/

```

But can we make it act on those "decisions"?

```ascii
> 🤖 Play Rocket Man cover by William Shatner in Rocket man on Spotify
```

<!-- note that's what we're gonna do today -->

<!-- fragments-end -->

---
<!-- classes: talk -->

# The plan 🤔

<!-- 1. Start chatting with OpenAI in a Python script
2. Connect to Azure's text-to-speech to have the AI read its answers aloud.
3. Add instructions to the system prompt to make the AI include syntax that we can parse, and use this to affect the text-to-speech voice.
4. Add more instructions to allow it to search for Spotify songs. -->

0. Get comfortable with the code base
1. Start chatting with OpenAI in a Python script
   - Tell it how to respond to you
   - Give it a personality
2. Give it a voice
3. Give it the power to do stuff
4. Keep building on it and add Spotify connection

---
<!-- classes: talk -->
<!-- qr: https://join.slack.com/share/enQtNjE3NTMwNDcwNjY5My05NzE1Y2Y3OGU3MTdlMjBkMDBhZjg5MmY3Yjk2NWU3MGNmNzQwOTNhOWEyOTQ0ZDExNTFlOTdmNTY4Y2E2OTdj -->
# #opkoko-diyassistant

- Link to repo
- Api-keys
- A place to show off what you've done

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
# One of these three should work

./.venv/Scripts/activate

source .venv/Scripts/activate

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

---
<!-- classes: talk -->

# Step-0: Setup

An `Assistance` is an object which you load with actions and then execute at the end.

```python
components/assitance.py

    class Assistance:
      assistance.addAction(...)
      assistance.exectue()
```

Add an action to the `assistance` object in `diy-assistant.py`

```python
assistance.addAction(lambda : print("Hello world"), "Print hello world")


assistance.addAction(lambda : os.startfile('C:/'), "Open file explorer")


assistance.addAction(lambda : os.system('shutdown -s'), "Shut down computer")
```

<!-- Make sure to give an overview of the code and that we have abstracted execution by the assistant to actions -->

---
<!-- classes: talk -->
# Step-1: Open AI

- System prompts are sent alongside message.
- Decide personality and behavior of AI.
- Best way to get it to stop being so clean, friendly and corporate.

Try making your own personality!

```bash
git merge 1-openai

# OR

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
# Step-2: Text to Speech

```bash
git merge 2-tts

# OR

git checkout 2-tts
```

Give your bot a voice!

New files in `components/azuretts.py`

Try new actions `speakText(text)` and `speakSSML(script)`.

---
<!-- classes: talk -->
# Parse chat output

```ascii
     ___________________________________________________________________
    / Yes, feeding your homework to you you dog is a good idea.         \
   / Here is a wikipedia page about the benefits of dogs eating homework \
🤖/\____________________________________________________________________/
```

Need a way to parse the text output into actions.

Instruct to respond in json-format

```json
{                                                                                   
    "message": "Yes, feeding your homework to you you dog is a good idea. Here is a
    wikipedia page about the benefits of dogs eating homework",                    
    "url": "https://en.wikipedia.org/wiki/The_Dog_Ate_My_Homework",                
}                                                                                  
```

---
<!-- classes: talk -->
# Step-3: Parser

Instruct OpenAI to provide text based instructions in a specific syntax, e.g. json.

```bash
git merge 3-parse

# OR

git checkout 3-parse
```

---
<!-- classes: talk -->
# Step-4: Spotify

```bash
git merge 4-spotify

# OR

git checkout 4-spotify
```

- Parse the output to another api-call.
- In this case, make it play music with spotify.
- If you want to participate, name and email registered to spotify account in #opkoko-diyassistant

---
<!-- classes: talk -->
# Recap

Code ❤️ OpenAI

Leverage creativity of LLM and provide it with natural language instructions which can be parsed using python code.

Today we:

1. Communicated with OpenAI
2. Give the assistant a voice
3. Parse text based instructions in specific syntax
4. Parse to additional api-calls, spotify

---
<!-- classes: talk -->
# Thanks

Go fourth and create the intelligent assistant and hope that they don't take you job!

👋
