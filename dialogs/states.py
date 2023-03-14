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
    event_dates = State()
    the_event = State()

    change_event = State()
    memes_input = State()

    event_delete_assure = State()
