from aiogram import types
import datetime


"""Inline-keyboard for asking a today's date"""
what_date_kb = types.InlineKeyboardMarkup(row_width=1)

what_date_bts = [
    types.InlineKeyboardButton(text=f"Is it today - {datetime.date.today()}?",
                               callback_data='yes'),
    types.InlineKeyboardButton(text="Some other day?",
                               callback_data="no")
]

what_date_kb.add(*what_date_bts)
