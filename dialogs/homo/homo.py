from aiogram import types

from main import dp
from database.bot_db import BotDB
from dialogs import states


@dp.message_handler(commands='gay')
async def gay(message: types.Message) -> None:
    """Test-function for saying that you're gay if you enter the specific command"""
    await message.answer("you're gay")


@dp.message_handler(commands="num")
async def get_event_num_test(message: types.Message) -> None:
    with BotDB() as db:
        event_num = db.get_new_event_number(message.from_user.id)

    await message.answer(str(event_num))
