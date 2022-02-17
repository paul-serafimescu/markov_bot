# Markov Bot

## About
A simple, *SINGLE SERVER* discord bot which tracks messages, processes them into a state transition graph, and utilizes markov chains to generate messages. 

## Setup
Place a `.env` file in your current working directory with the following values:
- `BOT_TOKEN`
    - the bot application token
- `ADMIN`
    - the `id` of the bot owner (your discord account id)
- `BOT_CHANNEL`
    - the channel `id` which you want the bot to be able to speak in 

## Running
To run, either place a `__main__.py` file in the `markov_bot` package and run accordingly:
```py
from bot import BotClient as MarkovBot
from config import BOT_TOKEN

if __name__ == '__main__':
    channels = [...]

MarkovBot(prefix='!', channels=channels).run(BOT_TOKEN)
```

Or you can do similar outside the package in your own module <small>(but do note that you need to change the absolute imports to relative imports per the Python module/package system)</small>:
```py
from markov_bot import MarkovBot
from markov_bot.config import BOT_TOKEN

if __name__ == '__main__':
    channels = [...]

MarkovBot(prefix='!', channels=channels).run(BOT_TOKEN)
```

## Issues
<small>Duly noted and ignored</small>
