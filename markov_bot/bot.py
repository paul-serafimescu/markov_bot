import discord
import ujson
import random
import time

from config import (
    SOURCE_FILE,
    DUMP_FILE,
    ADMIN,
    BOT_CHANNEL
)

class BotClient(discord.Client):
    def __init__(self, prefix: str, channels: list[int], train = True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open(SOURCE_FILE, 'r') as file:
            _data: dict[str, list[str]] = ujson.load(file)
            self.data = _data if _data is not None else {}
        self.prefix = prefix
        self.channels = channels
        self.last_command = time.time()
        self.train = train

    async def on_ready(self) -> None:
        print('bot is running...')

    def get_command(self, content: str) -> str | None:
        if content[:len(self.prefix)] == self.prefix:
            split_content = content.split()
            command = split_content[0][len(self.prefix):]
            return command
        else:
            return None

    def generate_response(self):
        keys = list(self.data)
        word = random.choice(keys)
        message = []
        while word != '\0':
            message.append(word)
            word = random.choice(self.data[word])
        return ' '.join(message)

    async def on_message(self, message: discord.Message) -> None:
        if not message.content or message.author.bot:
            return
        elif (command := self.get_command(message.content)) is not None:
            match command:
                case 'logout': 
                    if message.author.id == ADMIN:
                        with open(DUMP_FILE, 'w') as file:
                            ujson.dump(self.data, file)
                        return await self.close()
                case 'save':
                    if message.author.id == ADMIN:
                        with open(DUMP_FILE, 'w') as file:
                            ujson.dump(self.data, file)
                        return await message.channel.send('saved!')
                case 'gen':
                    current_time = time.time()
                    if message.channel.id == BOT_CHANNEL and current_time - self.last_command > 2:
                        self.last_command = current_time
                        return await message.channel.send(self.generate_response())
        elif message.channel.id in self.channels and self.train:
            words: list[str] = message.content.split()
            for word, next_word in zip(words, words[1:] + ['\0']):
                if self.data.get(word) is None:
                    self.data[word] = [next_word]
                else:
                    self.data[word].append(next_word)
        else:
            return
