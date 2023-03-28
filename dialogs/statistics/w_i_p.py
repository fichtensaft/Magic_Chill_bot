from aiogram import types
from aiogram.dispatcher.filters import Text

from main import dp


@dp.message_handler(Text(equals="Statistics 📊"))
async def start_randomizing(message: types.Message) -> None:
    """The starting of randomizing scenario. Although it does nothing now (work_in_progress)"""
    await message.answer(text="Statistics section is in development. Gonna be added soon", parse_mode="HTML")
