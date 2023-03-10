import operator

from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, Column, Group, Select, Multiselect
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput

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
        Button(
            Format("Сегодня - {date_today}?"),
            id="is_today",
            on_click=handlers.date_to_places
        ),
        Button(
            Const("Было в другой день"),
            id="not_today",
            on_click=handlers.next_state
        )
    ),
    getter=getters.date_getter,
    state=MemorizeEvent.date
)

"""
Window for the inputting your own date 
"""
date_input_window = Window(
    Const("Тогда нужна дата формата - день месяц год (через пробел):"),
    TextInput(
        id="date_input_text",
        type_factory=handlers.date_validation,
        on_success=handlers.date_success,
        on_error=handlers.date_failure
    ),
    state=MemorizeEvent.date_input
)

"""
Window for the 'Places' part of Memo-dialog
"""

places_kb = Select(
    Format("{item[0]}"),
    id="places_kb",
    item_id_getter=operator.itemgetter(1),
    items="places",
    on_click=handlers.places_to_friends  # The error in aiogram_dialog author's typehints?
)


places_window = Window(
    Const("Где мы собирались?"),
    Group(
        places_kb,
        Button(
            Const("Another 🌋..."),
            id="another_place",
            on_click=handlers.next_state
        ),
        width=2
    ),
    getter=getters.places_getter,
    state=MemorizeEvent.places
)


"""
Window for the  inputting your own place 
"""
places_input_window = Window(
    Const("Где же собирались? Введите место, пожольста:"),
    TextInput(
        id="place_input_text",
        on_success=handlers.place_success,
    ),
    state=MemorizeEvent.places_input
)


"""
Windows for the 'Friends' part of Memo-dialog
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
        on_click=handlers.friends_to_input
    ),
    Button(
        Const("That's all"),
        id="friends_end",
        on_click=handlers.friends_to_state
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
Creating of the friends_input part of the dialog
"""
friends_input_window = Window(
    Const("И кто эти чумбас? Введи через ';', будь лапочкой:"),
    TextInput(
        id="friends_input_text",
        type_factory=str,
        on_success=handlers.friends_input_success,
        # on_error=
    ),
    state=MemorizeEvent.friends_input
)

"""
Creating the state part of Memo-dialog
"""
state_window = Window(
    Const("В каком же вы состоянии, Херрен?"),
    Column(
        Button(
            Const("Sober 🧖‍♂️☕️🥒"),
            id="sober",
            on_click=handlers.state_to_memes
        ),
        Button(
            Const("Drunk 🍺🗿💨"),
            id="drunk",
            on_click=handlers.state_to_memes
        ),
    ),
    state=MemorizeEvent.state
)

"""
Creating the last - Memes part of Memo-dialog
"""
memes_window = Window(
    Const("Что по кекам?"),
    TextInput(
        id="memes_input_text",
        type_factory=str,
        on_success=handlers.memes_success
    ),
    state=MemorizeEvent.memes
)

"""
Registration of Memo-dialog
"""
memorize_windows = [
    date_window,
    date_input_window,
    places_window,
    places_input_window,
    friends_window,
    friends_input_window,
    state_window,
    memes_window
]
memorize_dialog = Dialog(*memorize_windows)
registry.register(memorize_dialog)
