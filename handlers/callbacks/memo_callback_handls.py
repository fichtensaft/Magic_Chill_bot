# from main import dp
# from aiogram import types
#
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
#
# from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
# from aiogram_dialog.widgets.kbd import Button, Multiselect, Column, Row, Group, Cancel
# from aiogram_dialog.widgets.text import Const, Format
#
# from loader import registry
# from keyboards.inline import memo_kb_inlines
#
#
# class MemorizeOld(StatesGroup):
#     """FSM-class for Memorizing an event (a meeting with friends)---scenario"""
#     date = State()
#     place = State()
#     people = State()
#     state = State()
#     memes = State()
#
#
# @dp.callback_query_handler(text="date_today")
# async def date_today(call: types.CallbackQuery) -> None:
#     """
#     Callback-handler for MEMO_PHASE_1:
#     If the user confirms that the needed day is TODAY
#     """
#     await call.message.answer("Okay, so it's today!\nWhere are you?",
#                               reply_markup=memo_kb_inlines.what_place_kb)
#     await call.answer()
#
#
# @dp.callback_query_handler(text="date_not_today")
# async def date_not_today(call: types.CallbackQuery, state: FSMContext) -> None:
#     """
#     Callback-handler for MEMO_PHASE_1:
#     If the user chooses to insert ANOTHER DAY
#     """
#     await call.message.answer("Введите дату форматом: дд мм гг (через пробел)")
#     await state.set_state(MemorizeOld.date.state)
#     await call.answer()
#
#
# @dp.message_handler(state=MemorizeOld.date)
# async def enter_the_date(message: types.Message, state: FSMContext) -> None:
#     """
#     Handler for taking an input of data from user (MEMO_PHASE_1)
#     """
#
#     await message.answer("Got your place\nWho is with us today?",
#                          reply_markup=memo_kb_inlines.what_people_kb)
#     await state.finish()
#
#
# @dp.callback_query_handler(Text(startswith="place"))
# async def which_place(call: types.CallbackQuery) -> None:
#     """
#     Callback-handler for MEMO_PHASE-2:
#     Where is user - dnd adding it to our date
#     """
#     len_place = 6
#     print(call.data[len_place:])
#     await call.message.answer("Got your place\nWho is with us today?",
#                               reply_markup=memo_kb_inlines.what_people_kb)
#     await call.answer()
