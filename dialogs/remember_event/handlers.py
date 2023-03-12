from time import strptime, strftime
from datetime import date

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
    await dialog_manager.start(state=RememberEvent.event_dates, mode=StartMode.RESET_STACK, data=message.from_user.id)


async def dates_to_the_event(callback: types.CallbackQuery, button: Button, dialog_manager: DialogManager,
                         *args) -> None:
    await dialog_manager.dialog().next()


# async def number_success(message: types.Message, enter: TextInput, dialog_manager: DialogManager, *args) -> None:
#     night_widget = dialog_manager.dialog().find("day_num_input")
#     try:
#         user_number = int(night_widget.get_value())
#         with BotDB() as db:
#             day_info = db.get_day_info(user_id=message.from_user.id, number=user_number)
#
#         await message.answer(text=day_info)
#     except ValueError:
#         print("Не вышло ='(")
#
#     await dialog_manager.done()






