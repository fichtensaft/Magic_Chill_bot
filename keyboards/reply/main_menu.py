from aiogram import types


"""Keyboard for main menu"""
main_menu_buttons = [
    types.KeyboardButton(text="Memorize an event 🗓️"),
    types.KeyboardButton(text="Randomize a song 🎲"),
]

main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
main_menu_keyboard.add(*main_menu_buttons)
