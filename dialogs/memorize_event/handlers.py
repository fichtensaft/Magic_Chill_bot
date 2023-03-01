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


# The 'input_date' part of Memo-dialog handlers:
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


async def to_places(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """Switching to the Places phase of the Memo-dialog"""
    await dialog_manager.dialog().switch_to(MemorizeEvent.places)


# Getting data from widgets handlers
async def get_friends_data(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager, *args) -> None:
    """
    Function for retrieving data from Widget(Window) - MultiSelector of Friends part of Memo-dialog
    // Right now it just prints it into the console
    """
    widget = dialog_manager.dialog().find("multi_friends")
    data = widget.get_checked()
    print(data)

    await dialog_manager.dialog().next()




