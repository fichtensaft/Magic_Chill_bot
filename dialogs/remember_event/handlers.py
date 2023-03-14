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


async def event_to_change(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                          *args) -> None:
    """Switching from the event window to changing this event"""
    await dialog_manager.dialog().switch_to(RememberEvent.change_event)


async def change_to_new_memes(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                              *args) -> None:
    """From choice of what to change to the memes changing window"""
    await dialog_manager.dialog().switch_to(RememberEvent.memes_input)


# Going-back handlers
async def the_event_to_dates(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                             *args) -> None:
    """Handler to go back from the exact event to the all event dates choice window"""
    await dialog_manager.dialog().back()


async def to_dates(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                   *args) -> None:
    await dialog_manager.dialog().switch_to(RememberEvent.event_dates)


async def dialog_done(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                      *args) -> None:
    """Ending the dialog"""
    await dialog_manager.done()


async def change_memes_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, args) -> None:
    """Function to add new memes to the already existing ones into the DataBase"""

    change_memes_widget = dialog_manager.dialog().find("change_memes_input")
    new_memes = change_memes_widget.get_value()

    with BotDB() as db:
        db.add_new_memes(new_memes=new_memes,
                         user_id=dialog_manager.current_context().start_data,
                         date=dialog_manager.current_context().dialog_data["event_date"])

    await message.answer("Added new memes to the event record, choom 🧐")
    await dialog_manager.dialog().switch_to(RememberEvent.the_event)


# Event-Delete section
async def change_to_assure_delete(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                                  *args) -> None:
    await dialog_manager.dialog().switch_to(RememberEvent.event_delete_assure)


async def delete_event(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                       *args) -> None:
    """Deleting the event altogether"""

    with BotDB() as db:
        db.delete_event(user_id=dialog_manager.current_context().start_data,
                        date=dialog_manager.current_context().dialog_data["event_date"])

    await callback.message.answer("The event was deleted, as you please 🐴\n Use the dates table to move on")
    await dialog_manager.dialog().switch_to(RememberEvent.event_dates)
