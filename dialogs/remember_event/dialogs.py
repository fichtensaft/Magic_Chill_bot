import operator

from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, Column, Group, Select, Multiselect, ScrollingGroup
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput

from loader import registry
from dialogs.states import RememberEvent
from dialogs.remember_event import getters
from dialogs.remember_event import handlers


"""
Window to start remembering the event day - Choose the exact event to remember
"""

event_dates_window = Window(
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
the_event_window = Window(
    state=RememberEvent.the_event

)


"""Registration of the Remember-Dialog windows"""
remembering_windows = [
    event_dates_window
]
event_dates_dialog = Dialog(*remembering_windows)
registry.register(event_dates_dialog)

