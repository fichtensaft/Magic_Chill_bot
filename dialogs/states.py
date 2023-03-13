from aiogram.dispatcher.filters.state import State, StatesGroup


class MemorizeEvent(StatesGroup):
    """
    FSM-class for Memorizing an event (a meeting with friends)---scenario
    For aiogram-dialogs also
    """
    date = State()
    date_input = State()

    places = State()
    places_input = State()

    friends = State()
    friends_input = State()

    state = State()
    memes = State()


class RememberEvent(StatesGroup):
    choose_state = State()
    by_state_event_dates = State()
    all_event_dates = State()
    the_event = State()
