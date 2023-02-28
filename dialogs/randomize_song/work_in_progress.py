from aiogram import types
from aiogram.dispatcher.filters import Text

from main import dp


@dp.message_handler(Text(equals="Randomize a song 🎲"))
async def start_randomizing(message: types.Message) -> None:
    """The starting of randomizing scenario. Although it does nothing now (work_in_progress)"""
    await message.answer(text="Находится в разработке. Пока рандом песен недоступен. Но будет <b>восстановлен!</b>",
                         parse_mode="HTML")