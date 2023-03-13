import operator

from aiogram.types import ParseMode

from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, Column, Group, Select, Multiselect, ScrollingGroup
from aiogram_dialog.widgets.text import Const, Format, Jinja
from aiogram_dialog.widgets.input import TextInput

from loader import registry
from dialogs.states import RememberEvent
from dialogs.remember_event import getters
from dialogs.remember_event import handlers


"""
Window to choose which state we're looking into
"""
choose_state_window = Window(
    Const("Human, what state are we looking for?"),
    Column(
        Button(
            Const("Sober 🧘‍♀️🌲🪐"),
            id="fetch_sober",
            on_click=handlers.choose_to_dates,
        ),
        Button(
            Const("Drunk 🍻🤙🪨"),
            id="fetch_drunk",
            on_click=handlers.choose_to_dates,

        ),
        Button(
            Const("Sober&Drunk 🚀"),
            id="fetch_both",
            on_click=handlers.choose_to_dates,

        ),
    ),
    state=RememberEvent.choose_state
)

"""
Window to show event days. With pre-made choice (past window) of state  
"""
all_event_dates_window = Window(
    Const("Choose the day to remember:"),
    ScrollingGroup(
        Select(
            Format("{item[0]}"),
            id="event_dates_kb",
            item_id_getter=operator.itemgetter(1),
            items="dates",
            on_click=handlers.dates_to_the_event
        ),
        id="event_dates_scroll",
        width=4,
        height=5

    ),
    state=RememberEvent.event_dates,
    getter=getters.dates_getter
)

"""
Window to look into the exact event
"""
# We get the tuple like: (5, '2023-03-11', 'drunk', 'Иля; Потап', 'Po-Lounge', 'Оксид алюминия (химические реакции, термит); \nМне срут на лицо (journey 💩) - Гражданская Оборона; \nМикроконтроллеры')
the_event_window = Window(
    Format(
        "<b>Number of event</b>: {event_info[0]}\n"
        "<b>Date</b>: {event_info[1]}\n"
        "<b>State</b>: {event_info[2]}\n"
        "<b>Place</b>: {event_info[4]}\n"
        "<b>People</b>: {event_info[3]}\n"
        "<b>Memes</b>:\n"
        "{event_info[5]}"
    ),
    state=RememberEvent.the_event,
    getter=getters.event_info_getter,
    parse_mode=ParseMode.HTML

)

"""Registration of the Remember-Dialog windows"""
remembering_windows = [
    choose_state_window,
    all_event_dates_window,
    the_event_window
]
event_dates_dialog = Dialog(*remembering_windows)
registry.register(event_dates_dialog)

