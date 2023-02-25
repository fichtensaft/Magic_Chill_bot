from main import dp
from aiogram import types


@dp.message_handler(commands='gay')
async def gay(message: types.Message) -> None:
    """Test-function for saying that you're gay if you enter the specific command"""
    await message.answer("you're gay")
