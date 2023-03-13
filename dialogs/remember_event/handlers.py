from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput

from main import dp
from database.bot_db import BotDB
from dialogs.states import RememberEvent


@dp.message_handler(Text(equals="Remember events 💭"))
async def start_remembering(message: types.Message, dialog_manager: DialogManager) -> None:
    """Starting Remembering_Event-scenario"""
    await dialog_manager.start(state=RememberEvent.choose_state, mode=StartMode.RESET_STACK, data=message.from_user.id)


async def choose_to_dates(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                          *args) -> None:
    """Choosing a state we're looking into and passing a callback date to getter, so we can get the exact event days"""

    state = callback.data.lstrip("fetch_")
    dialog_manager.current_context().dialog_data["state"] = state
    await dialog_manager.dialog().switch_to(RememberEvent.event_dates)


async def dates_to_the_event(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                             *args) -> None:
    """
    Choosing an event-date so we can pass a data to the getter and fetch info about the event
    """
    event_date = callback.data.lstrip("event_dates_kb:")
    dialog_manager.current_context().dialog_data["event_date"] = event_date

    await dialog_manager.dialog().switch_to(RememberEvent.the_event)
