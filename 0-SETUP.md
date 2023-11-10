# STEP 0: SETUP

## 1. Install python dependencies

If you wish to isolate the packages in a separate virtual environment you can use `python -m venv .venv` and then activate it using `./.venv/Scripts/activate` or `source .venv/Scripts/activate` or `source .venv/bin/active`. To leave the environment, after the lab, run the command `deactivate`.

Continue by installing all required packages `pip install -r requirements.txt`.

If it fails it can help to run `pip install --upgrade pip setuptools wheel` and then running

## 2. Set up env

Copy `.env.example` to a new file called `.env` and replace the placeholders.

## 3. Test the application

Try running `py diy-assistant.py`.

Look around in `assistant` and `components/assistance.py`

The structure of this project is based on creating an "Assistance" and loading it with callbacks that can be called by the main assistant script. This is to give more freedom for the individual parsers to decide how the assistant acts.

## 4. Add an action

Add another, simple action to the assistant to test the functionality.

## Go to next step

Checkout branch `1-openai`.
