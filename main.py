import logging

from aiogram import executor
from loader import dp

# without this import handlers, dialog, etc. just don't work
import dialogs

# Activation of logging
logging.basicConfig(level=logging.INFO)

# Activation of the bot polling
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
