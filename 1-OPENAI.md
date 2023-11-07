# STEP 1: OPENAI

## 1. Check out the new files

A new file `components/chat.py` has been added which contains the code for communicating with OpenAI which `assitant.py` has integrated with.
There are also system prompts placed in `components/system-prompts/`.

Run the application again using `py assistant.py` and try out chatting with it.

## 2. Write a system prompt

System prompts are sent alongside your message to structure and decide the behaviour of the responses you will get. This is where your AI will get its personality and is usually the best way to get it to stop being so clean, friendly and corporate.

There are examples in `components/system-prompts/examples`, but you can also find examples in the [mustvlad/ChatGPT-System-Prompts](https://github.com/mustvlad/ChatGPT-System-Prompts) repo on GitHub.

Some tips from my experience:

- Telling it that is is an actor or playing a character is a good way to give it a stronger personality.
- Telling it to never break character will prevent it from reverting to it's regular mode when it doesn't understand.
- Listing rules is a good way to structure the system prompt.
- It can be good to tell it to keep itself short. It tends to ramble (which makes for very long text-to-speech files).
- Examples can help it understand how to structure its answers.

## 3. Reflect

We'll talk about what we personally felt made for a good system prompt and share tips.

## Go to next step

Checkout branch `2-tts`.
