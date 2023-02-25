from aiogram import types

from aiogram_dialog import Window, Dialog, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Column, Cancel
from aiogram_dialog.widgets.text import Const, Format

from main import dp
from loader import registry
from .getters import date_getter
from dialogs.states import MemorizeEvent


"""Dialog Window (keyboard) for asking a today's date"""
date_window = Window(
    Const("Когда собирались?"),
    Column(
        Button(Format("Сегодня - {date_today}?"), id="is_today"),
        Button(Const("Было в другой день"), id="not_today")),
    getter=date_getter,
    state=MemorizeEvent.date
)

date_dialog = Dialog(date_window)
registry.register(date_dialog)
