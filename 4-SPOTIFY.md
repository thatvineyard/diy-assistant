# STEP 4: SPOTIFY

## 1. This time we don't need new files

The goal for this step is to use the provided Spotify library (which has been added to `assistant.py`) to have the AI affect things other than its speech.

> Note: The plan was to have the AI control your Spotify account but the time ran out, so we can only do non-account related things such as search

First off we want to update our system prompt so it gives us a keyword to search for in a specific syntax. You can look at `components/system-prompts/examples/spotify-prompt.txt` for inspiration.

Then we want to parse the answer, search using the given keyword, and replace that keyword with the first result.

For example:

> "I love this new song called **[trending on tiktok]** that I found completely by myself"

should turn into

> "I love this new song called **Lemon Pound Cake** that I found completely by myself".

The Spotify library can be used the following way:

```python
results = spotipy.search(bracketWord.group(1), 1)
track = results['tracks']['items'][0]
name = track['name']
```

Read about the structure of the result [here](https://developer.spotify.com/documentation/web-api)

For inspiration you can look at `components/chatparsers/spotifyparser.py`, but be warned that I wrote it late at night 3 hours after I thought I would be done. 

## That's it

Hopefully it didn't take too long.

Now it's up to you to be creative and figure out something else it can do. Some ideas are:

- Have it write your git commit messages while it tells you how proud it is of you
- Have it play chess while taunting you incessantly
- Have it create animations in real time using some sort of graphics library
- Have it turn off Elden Ring every time you die unless you manage to convince it that you're actually getting better

## Further reading

- https://medium.com/coinmonks/top-20-chatgpt-prompts-that-every-prompt-engineers-should-know-937b0ea5472#14a6
- https://www.promptingguide.ai/introduction/examples
- https://github.com/mustvlad/ChatGPT-System-Prompts
