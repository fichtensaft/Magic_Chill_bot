from main import dp
from aiogram import types


@dp.callback_query_handler(text="yes")
async def test(call: types.CallbackQuery):
    await call.message.answer("Okay, so it's today!")