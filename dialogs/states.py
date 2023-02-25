from aiogram.dispatcher.filters.state import State, StatesGroup


class MemorizeEvent(StatesGroup):
    """
    FSM-class for Memorizing an event (a meeting with friends)---scenario
    For aiogram-dialogs also
    """
    date = State()
    place = State()
    people = State()
    state = State()
    memes = State()

