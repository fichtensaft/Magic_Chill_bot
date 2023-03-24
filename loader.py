from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram_dialog import DialogRegistry

from os import getenv
from sys import exit

from database.bot_db import BotDB
from config import TOKEN


# Creating a memory storage to use in the bot (in the dispatcher)
# Right now only for RAM
storage = MemoryStorage()

# Creating a DataBase instance (also created a db via its method) //creating & dropping
db = BotDB()
# db.drop_table_events()
# db.alter_table()
# db.create_events_table()

# Making the bot-object and his dispatcher
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=storage)

# Creating a register to... register Dialogs for lib: "aiogram-dialog"
registry = DialogRegistry(dp)
