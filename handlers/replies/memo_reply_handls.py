from main import dp

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import inline


@dp.message_handler(Text(equals="Randomize a song 🎲"))
async def start_randomizing(message: types.Message) -> None:
    """Function for starting the MEMORIZING-scenario"""
    await message.answer(text="The block with songs was deleted due to enterprise issues\n"
                              "Soon will be <b>restored!</b>")
