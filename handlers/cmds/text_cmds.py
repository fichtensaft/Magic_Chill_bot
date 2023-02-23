from main import dp
from aiogram import types

from keyboards import reply


@dp.message_handler(commands='start')
async def start(message: types.Message) -> None:
    """Function for the activation of the Chill Bot"""
    await message.answer("Hey, I'm working now! Wanna some magic chilling?",
                         reply_markup=reply.main_menu.main_menu_keyboard)


@dp.message_handler(commands='gay')
async def gay(message: types.Message) -> None:
    """Test-function for saying that you're gay if you enter the specific command"""
    print('gay is printing')
    await message.answer("you're gay")


# @dp.message_handler()
# async def echo_gay(message: types.Message) -> None:
#     """Test - !!!ECHO!!! - function for naming everyone gay"""
#     await message.answer("YOU ARE GAAAAAAY")
