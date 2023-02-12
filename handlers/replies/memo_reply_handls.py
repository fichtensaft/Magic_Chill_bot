from main import dp

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import inline


@dp.message_handler(Text(equals="Memorize an event 🗓️"))
async def start_memorizing(message: types.Message):
    await message.answer(text="What's the day?", reply_markup=inline.memo_kb_inlines.what_date_kb)
