from aiogram import types

import datetime


"""Inline-keyboard for asking a today's date"""
what_date_kb = types.InlineKeyboardMarkup(row_width=1)
what_date_bts = [
    types.InlineKeyboardButton(text=f"Is it today - {datetime.date.today().strftime('%d/%m/%y')}?",
                               callback_data='date_today'),
    types.InlineKeyboardButton(text="Some other day?",
                               callback_data="date_not_today")
]

what_date_kb.add(*what_date_bts)


"""Inline-keyboard for asking for place"""
what_place_kb = types.InlineKeyboardMarkup(row_width=2)
what_place_bts = [
    types.InlineKeyboardButton(text="Quarry 🦦", callback_data="place Quarry"),
    types.InlineKeyboardButton(text="Shaman lair 🛖", callback_data="place Shaman lair"),
    types.InlineKeyboardButton(text="Hideout 🔬", callback_data="place Hideout"),
    types.InlineKeyboardButton(text="Casa grande 🦄", callback_data="place Casa grande"),
    types.InlineKeyboardButton(text="Po-Lounge ⚙️", callback_data="place Po-Lounge"),
    types.InlineKeyboardButton(text="Le Garage 🏴‍☠️", callback_data="place Le Garage"),
    types.InlineKeyboardButton(text="The forest 🌳", callback_data="place The forest"),
    types.InlineKeyboardButton(text="Other...", callback_data="other")
]

what_place_kb.add(*what_place_bts)


"""Inline-keyboard for the present people"""
what_people_kb = types.InlineKeyboardMarkup(row_width=3)
what_people_bts = [
    types.InlineKeyboardButton(text="Иля 🧙‍♂️", callback_data="people_Иля"),
    types.InlineKeyboardButton(text="Кирилл 🕵️", callback_data="people_Кирилл"),
    types.InlineKeyboardButton(text="Потап 👨‍🏭", callback_data="people_Потап"),
    types.InlineKeyboardButton(text="Олегсий 👨‍🌾", callback_data="people_Олегсий"),
    types.InlineKeyboardButton(text="Диман 🧑‍🍳", callback_data="people_Диман"),
    types.InlineKeyboardButton(text="Паша 🧟‍♂️", callback_data="people_Паша"),
    types.InlineKeyboardButton(text="Лёня 👷🏻‍♂️", callback_data="people_Лёня"),
    types.InlineKeyboardButton(text="Other...", callback_data="people_other"),
    types.InlineKeyboardButton(text="End 🎬", callback_data="people_end")
]

what_people_kb.add(*what_people_bts)
