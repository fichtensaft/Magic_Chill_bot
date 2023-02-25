from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram_dialog import DialogManager, StartMode

from main import dp
from dialogs.states import MemorizeEvent


@dp.message_handler(Text(equals="Memorize an event 🗓️"))
async def start_memorizing(message: types.Message, dialog_manager: DialogManager) -> None:
    """Function for starting the MEMORIZING-scenario"""
    await dialog_manager.start(state=MemorizeEvent.date, mode=StartMode.RESET_STACK)
