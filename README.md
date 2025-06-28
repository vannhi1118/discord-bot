# Discord-Bot

## Summary
This is a quick implementation of a WordChain Discord bot for Vietnamese, with some basic functions
- User enters a composite word to start
- Check if user is the last user
- Validate words
    - The word must be a composite word of 2 words. If more then ignore
    - First word matching the previous last word
    - That word must exist in the dictionary
    - Word has not been used in that round
- React to inform user is the word is acceptable/used/invalid

## Setup 
1. Create a new bot application on Discord Developer Portal and get the token
2. Create a `.env` file to save your token
```
DISCORD_TOKEN=<YOUR TOKEN>
```
3. (Optional) Create a virtual environment to install required python packages
4. Run `pip install -r requirements.txt`
5. (Optional/Might Need) Add pythonpath to avoid module errors by running this command
`export PYTHONPATH=$PYTHONPATH:<full path to discord-bot/src>`

## Run
Run `python bot.py` 
