from main import dp
from aiogram import types
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.inline import memo_kb_inlines


ppl_list = []


class MemorizeDate(StatesGroup):
    """FSM-class for MEMO-scenario"""
    waiting_for_date = State()
    waiting_for_place = State()
    waiting_for_people = State()



@dp.callback_query_handler(text="date_today")
async def date_today(call: types.CallbackQuery) -> None:
    """
    Callback-handler for MEMO_PHASE_1:
    If the user confirms that the needed day is TODAY
    """
    await call.message.answer("Okay, so it's today!\nWhere are you?",
                              reply_markup=memo_kb_inlines.what_place_kb)
    await call.answer()


@dp.callback_query_handler(text="date_not_today")
async def date_not_today(call: types.CallbackQuery) -> None:
    """
    Callback-handler for MEMO_PHASE_1:
    If the user chooses to insert another day
    """
    await call.message.answer("!!!WORK IN PROGRESS!!!")
    await call.answer()


@dp.callback_query_handler(Text(startswith="place"))
async def which_place(call: types.CallbackQuery) -> None:
    """
    Callback-handler for MEMO_PHASE-2:
    Where is user - dnd adding it to our date
    """
    len_place = 6
    print(call.data[len_place:])
    await call.message.answer("Got your place\nWho is with us today?",
                              reply_markup=memo_kb_inlines.what_people_kb)
    await call.answer()


@dp.callback_query_handler(Text(startswith="people"))
async def which_people(call: types.CallbackQuery) -> None:
    """
    Callback-handler for MEMO_PHASE-#2:
    Who's chilling with me today?
    """
    human = call.data.split('_')[1]
    if human == 'end':
        await call.message.answer(f"Эти ребятишки на празднике чилла: {ppl_list}")
        await call.answer()
    if human not in ppl_list and human not in ["end", "other"]:
        ppl_list.append(human)
        await call.answer()



