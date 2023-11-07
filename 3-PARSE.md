# STEP 3: PARSE

## 1. Check out the new files

We have yet a new file: `components/parser.py`. It is a blank parser that just creates an `Assitance` like we did in the previous step.

## 2. Write a parser

Your job is to create some sort of logic in there that makes use of what the AI answers. But before we do that we should think about what we want the AI to answer to help us.

By asking it to include directions in a specific syntax (like in square brackets, delimited by a certain character or something like that) we can then read it. For some tips, read this [article](https://medium.com/coinmonks/top-20-chatgpt-prompts-that-every-prompt-engineers-should-know-937b0ea5472#14a6)

There are also examples in `components/chatparsers` that have their corresponding system prompts in `compontnets/system-prompts`. These are the parsers I build when prototyping the workshop. They have some flaws, but so do we all.

## Go to next step

Checkout branch `4-spotify`.
