import operator

from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, Column, Group, Select, Multiselect
from aiogram_dialog.widgets.text import Const, Format

from loader import registry
from dialogs.states import MemorizeEvent
from dialogs.memorize_event import getters
from dialogs.memorize_event import handlers

# Creating a 'Memorize_Event Dialog' and its Windows, etc.
"""
Window for the 'Date' part of Memo-dialog
"""
date_window = Window(
    Const("Когда собирались?"),
    Column(
        Button(Format("Сегодня - {date_today}?"),
               id="is_today",
               on_click=handlers.next_state),
        Button(Const("Было в другой день"), id="not_today")),
    getter=getters.date_getter,
    state=MemorizeEvent.date
)

"""
Window for the 'Places' part of Memo-dialog
"""

places_kb = Select(
    Format("{item[0]}"),
    id="place_kb",
    item_id_getter=operator.itemgetter(1),
    items="places",
    on_click=handlers.next_state  # The error in author's typehints?
)

places_window = Window(
    Const("Где мы собирались?"),
    Group(
        places_kb,
        width=2
    ),
    getter=getters.places_getter,
    state=MemorizeEvent.place
)

"""
Window for the 'Friends' part of Memo-dialog
"""
# Keyboard for people to choose from
friends_kb_ppl = Multiselect(
    checked_text=Format("✓ {item[0]}"),
    unchecked_text=Format("{item[0]}"),
    id="multi_friends",
    item_id_getter=operator.itemgetter(1),
    items="friends"
)

# Bottom keyboard to end interaction with this window or to input some other people (FUTURE)
friends_kb_options = Group(
    Button(
        Const("Some others"),
        id="friends_others",
        # on_click=
    ),
    Button(
        Const("That's all"),
        id="friends_end",
        on_click=handlers.retrieve_friends_data
    )
)

# Creating of the friends_window itself
friends_window = Window(
    Const("Who was with us?"),
    Group(
        friends_kb_ppl,
        friends_kb_options,
        width=3
    ),
    getter=getters.get_friends,
    state=MemorizeEvent.friends
)

"""
Registration of Memo-dialog
"""
memorize_dialog = Dialog(*[date_window, places_window, friends_window])
registry.register(memorize_dialog)
