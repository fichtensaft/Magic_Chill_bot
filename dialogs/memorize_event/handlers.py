from time import strptime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput

from main import dp
from dialogs.states import MemorizeEvent


# Starting a Memorize-dialog scenario
@dp.message_handler(Text(equals="Memorize an event 🗓️"))
async def start_memorizing(message: types.Message, dialog_manager: DialogManager) -> None:
    """Function for starting the MEMORIZING-scenario"""
    await dialog_manager.start(state=MemorizeEvent.date, mode=StartMode.RESET_STACK)


# The 'date_input' part of Memo-dialog handlers:
def date_validation(user_date: str, date_format='%d %m %y') -> None:
    """
    Function to check if the user date is correct
    If it fails, ValueError is raised (in the result of 'strptime' function) and aiogram_dialog type_factory handles it,
    so it's an automatic success or error (in TextInput widget)
    :param user_date (str) -> waiting for a date from user
    :param date_format (str) -> module 'time' format to check the date
    """
    valid_date = strptime(user_date, date_format)


async def date_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """If the date_input is valid, the func moves to the next part (places) of Memo-dialog"""
    await message.answer(text="Отлично, идём дальше!")
    await dialog_manager.dialog().next()


async def date_failure(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """If the date_input is invalid, the user has to input date again"""
    await message.answer(text="Введённая формат даты неверен. Повторите, пожалуйста-с")


# The 'places_input' part of Memo-dialog handlers:

async def place_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """Takes another place from the user's input"""
    await message.answer(text="Интересное местечко")
    await dialog_manager.dialog().next()


# The 'friends_input' part of Memo-dialog handlers:

async def friends_input_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    """On Friends TextInput success (should be always, though)"""
    widget=dialog_manager.dialog().find("friends_input_text")
    data = widget.get_value().split(';')

    for i in data:
        print(i, end=' --> ')

    await message.answer("Прекрасные люди. Давай дальше")
    await dialog_manager.dialog().next()


# The 'memes' part of Memo-dialog handlers
async def memes_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
    widget = dialog_manager.dialog().find("memes_input_text")
    data = widget.get_value()
    print(data)

    await message.answer("Как кекно")
    await dialog_manager.done()


# Transition handlers
async def next_state(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """Switching to the next phase of the Memo-dialog"""
    print(button.widget_id)
    await dialog_manager.dialog().next()


async def date_to_places(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """Switching to the Places phase of the Memo-dialog"""
    await dialog_manager.dialog().switch_to(MemorizeEvent.places)


async def places_to_friends(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """Switching to the Friends phase of the Memo-dialog (after choosing any given place)"""
    await dialog_manager.dialog().switch_to(MemorizeEvent.friends)


# Getting data from widgets handlers
async def friends_to_state(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """
    Function for retrieving data from Widget(Window) - MultiSelector of Friends part of Memo-dialog
    // Right now it just prints it into the console
    """
    widget = dialog_manager.dialog().find("multi_friends")
    data = widget.get_checked()
    print(data)

    await dialog_manager.dialog().switch_to(MemorizeEvent.state)




