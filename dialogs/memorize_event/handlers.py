from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.manager.protocols import ManagedWidgetProto

from main import dp
from dialogs.states import MemorizeEvent


@dp.message_handler(Text(equals="Memorize an event 🗓️"))
async def start_memorizing(message: types.Message, dialog_manager: DialogManager) -> None:
    """Function for starting the MEMORIZING-scenario"""
    await dialog_manager.start(state=MemorizeEvent.date, mode=StartMode.RESET_STACK)


async def next_state(callback: types.CallbackQuery,button: Button, dialog_manager: DialogManager, *args) -> None:
    """Switching to the next phase of the Memo-dialog"""
    await dialog_manager.dialog().next()


async def retrieve_friends_data(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager) -> None:
    """
    Function for retrieving data from Widget(Window) - MultiSelector of Friends part of Memo-dialog
    // Right now it just prints it into the console
    """
    widget = dialog_manager.dialog().find("multi_friends")
    data = widget.get_checked()
    print(data)
