from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram_dialog import DialogRegistry

from os import getenv
from sys import exit

# Getting a bot_token from env_variables
bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

# Creating a memory storage to use in the bot (in the dispatcher)
# Right now only for RAM
storage = MemoryStorage()

# Making the bot-object and his dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher(bot=bot, storage=storage)

# Creating a register to... register Dialogs for lib: "aiogram-dialog"
registry = DialogRegistry(dp)
