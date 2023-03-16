from main import dp
from aiogram import types


"""Keyboard for main menu"""
main_menu_buttons = [
    types.KeyboardButton(text="Memorize an event 🗓️"),
    # types.KeyboardButton(text="Randomize a song 🎲"),
    types.KeyboardButton(text="Remember events 💭"),
    # types.KeyboardButton(text="Statistics 📊")
]
main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
main_menu_keyboard.add(*main_menu_buttons)


@dp.message_handler(commands='start')
async def start(message: types.Message) -> None:
    """Function for the activation of the Chill Bot"""
    await message.answer("Hey, choomba! Wanna some magic chilling?",
                         reply_markup=main_menu_keyboard)

