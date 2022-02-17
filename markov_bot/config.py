import dotenv
import os

from pathlib import Path

dotenv.load_dotenv(os.path.join(os.getcwd(), '.env'))

BOT_TOKEN = os.environ.get('BOT_TOKEN')

DUMP_FILE = os.path.join(os.getcwd(), 'data.json')
Path(DUMP_FILE).touch(exist_ok = True)
SOURCE_FILE = os.path.join(os.getcwd(), 'data.json')
Path(SOURCE_FILE).touch(exist_ok = True)
ADMIN = int(os.environ.get('ADMIN'))
BOT_CHANNEL = 943781988538671165
