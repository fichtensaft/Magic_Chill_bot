from time import strptime, strftime
from datetime import date

from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput

from main import dp
from database.bot_db import BotDB
from dialogs.states import MemorizeEvent


# Starting a Memorize-dialog scenario
@dp.message_handler(Text(equals="Memorize an event 🗓️"))
async def start_memorizing(message: types.Message, dialog_manager: DialogManager) -> None:
    """Function for starting the MEMORIZING-scenario"""
    await dialog_manager.start(state=MemorizeEvent.date, mode=StartMode.RESET_STACK)


# The 'date' part of Memo-dialog handlers:
async def date_to_places(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                         *args) -> None:
    """Switching to the Places phase of the Memo-dialog"""
    today = date.today().strftime('%Y-%m-%d')
    dialog_manager.current_context().dialog_data["date"] = today

    await dialog_manager.dialog().switch_to(MemorizeEvent.places)


def date_validation(user_date: str, date_format='%d %m %y') -> None:
    """
    Function to check if the user date is correct
    If it fails, ValueError is raised (in the result of 'strptime' function) and aiogram_dialog type_factory handles it
    """
    valid_date = strptime(user_date, date_format)


async def date_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """If the date_input is valid, the func moves to the next part (places) of Memo-dialog"""

    date_from_user = strptime(message.text, "%d %m %y")  # Getting a date from user and converting it for SQlite
    converted_date = strftime("%Y-%m-%d", date_from_user)
    dialog_manager.current_context().dialog_data["date"] = converted_date

    await message.answer(text="Отлично, идём дальше!")
    await dialog_manager.dialog().next()


async def date_failure(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """If the date_input is invalid, the user has to input date again"""
    await message.answer(text="Введённая формат даты неверен. Повторите, пожалуйста-с")


# The 'places' part of Memo-dialog handlers:
async def places_to_friends(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                            *args) -> None:
    """Switching to the Friends phase of the Memo-dialog (after choosing any given place)"""
    if callback.data != "another_place":
        dialog_manager.current_context().dialog_data["place"] = callback.data.lstrip("places_kb:")
    await dialog_manager.dialog().switch_to(MemorizeEvent.friends)


async def place_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """Takes another place from the user's input"""
    place_input_widget = dialog_manager.dialog().find("place_input_text")
    user_place = place_input_widget.get_value()
    dialog_manager.current_context().dialog_data["place"] = user_place

    await message.answer(text="Интересное местечко")
    await dialog_manager.dialog().next()


# The 'friends' part of Memo-dialog handlers:
async def friends_to_state(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """
    Function for retrieving data from Widget(Window) - MultiSelector of Friends part of Memo-dialog
    // Right now it just prints it into the console
    """
    multi_friends_widget = dialog_manager.dialog().find("multi_friends")
    multi_friends_data = multi_friends_widget.get_checked()
    dialog_manager.current_context().dialog_data["friends"] = multi_friends_data

    await dialog_manager.dialog().switch_to(MemorizeEvent.state)


async def friends_to_input(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """
    Switching to text input from choosing friends of Multiselect
    """
    multi_friends_widget = dialog_manager.dialog().find("multi_friends")
    multi_friends_data = multi_friends_widget.get_checked()
    dialog_manager.current_context().dialog_data["friends"] = multi_friends_data

    await dialog_manager.dialog().next()


async def friends_input_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """On Friends TextInput success (should be always, though)"""
    friends_input_widget = dialog_manager.dialog().find("friends_input_text")
    other_friends = friends_input_widget.get_value().split(";")

    dialog_manager.current_context().dialog_data["friends"].extend(other_friends)

    await message.answer("Прекрасные люди. Давай дальше")
    await dialog_manager.dialog().next()


# The 'state' part of Memo-dialog handlers
async def state_to_memes(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    dialog_manager.current_context().dialog_data["state"] = callback.data
    await dialog_manager.dialog().next()


# The 'memes' part of Memo-dialog handlers
async def memes_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """Input of memes of the event from user"""

    memes_widget = dialog_manager.dialog().find("memes_input_text")  # Getting data from user's input
    memes_data = memes_widget.get_value()
    dialog_manager.current_context().dialog_data["memes"] = memes_data
    # print(*dialog_manager.current_context().dialog_data.values())

    dialog_manager.current_context().dialog_data["friends"] = " ;".join(
        dialog_manager.current_context().dialog_data.get("friends")
    )
    data = dialog_manager.current_context().dialog_data.values()
    print(*dialog_manager.current_context().dialog_data.values())

    with BotDB() as db:
        db.insert_memo_values(message.from_user.id, db.get_new_event_number(message.from_user.id), *data)

    await message.answer("Как кекно")
    await dialog_manager.done()


# Transition-handlers
async def next_state(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    await dialog_manager.dialog().next()
