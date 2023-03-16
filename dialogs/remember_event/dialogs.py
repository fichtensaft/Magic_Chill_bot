import operator

from aiogram.types import ParseMode

from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, Column, Row, Group, Select, ScrollingGroup
from aiogram_dialog.widgets.text import Const, Format
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
    Row(
        Button(
            Const("Back to states ⬅️"),
            id="event_dates_back_but",
            on_click=handlers.dialog_back
        ),
        Button(
            Const("Thx, enough 👌"),
            id="event_dates_done_but",
            on_click=handlers.dialog_done
        )
    ),
    state=RememberEvent.event_dates,
    getter=getters.dates_getter
)

"""
Window to look into the exact event
"""
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
    Column(
        Button(
            Const("Change event info 📝"),
            id="but_change_event",
            on_click=handlers.event_to_change
        ),
        Button(
            Const("Back to the dates ⬅️"),
            id="but_event_to_dates",
            on_click=handlers.the_event_to_dates
        ),
        Button(
            Const("Enough, thx 👌"),
            id="event_to_end",
            on_click=handlers.dialog_done
        )
    ),
    state=RememberEvent.the_event,
    getter=getters.event_info_getter,
    parse_mode=ParseMode.HTML

)

"""
Window to change the event info
"""
change_event_window = Window(
    Const("What part do you want to change?"),
    Group(
        Button(
            Const("New memes! 😎"),
            id="new_memes_but",
            on_click=handlers.change_to_add_memes
        ),
        Button(
            Const("Add people 🤼‍♂️"),
            id="add_ppl_but",
            on_click=handlers.change_to_add_ppl
        ),
        Button(
            Const("Add places 🏘"),
            id="add_places_but",
            on_click=handlers.change_to_add_places
        ),
        Button(
            Const("Delete the event 💀"),
            id="delete_event_but",
            on_click=handlers.change_to_assure_delete
        ),
        width=2
    ),
    state=RememberEvent.change_event,
    getter=getters.change_event_getter
)

"""
Window to input memes
"""
add_memes_window = Window(
    Const("What memes are we talking about?"),
    TextInput(
        id="add_memes_input",
        on_success=handlers.add_memes_success
    ),
    state=RememberEvent.memes_input
)

"""
Window to input people 
"""
add_ppl_window = Window(
    Const("What people are joining the party? 🎉 "),
    TextInput(
        id="add_ppl_input",
        on_success=handlers.add_ppl_success
    ),
    state=RememberEvent.ppl_input
)

"""
Window to input places 
"""
add_places_window = Window(
    Const("Where else have you been? 🏡"),
    TextInput(
        id="add_places_input",
        on_success=handlers.add_places_success
    ),
    state=RememberEvent.places_input
)
"""
Window to assure the deletion of the event 
"""
assure_delete_window = Window(
    Const("Are you sure?"),
    Row(
        Button(
            Const("Yes ✅"),
            id="sure_yes_but",
            on_click=handlers.delete_event
        ),
        Button(
            Const("No ❌"),
            id="sure_no_but",
            on_click=handlers.to_dates
        )
    ),
    state=RememberEvent.event_delete_assure
)

"""Registration of the Remember-Dialog windows"""
remembering_windows = [
    choose_state_window,
    all_event_dates_window,
    the_event_window,

    change_event_window,
    add_memes_window,
    add_ppl_window,
    add_places_window,
    assure_delete_window
]
event_dates_dialog = Dialog(*remembering_windows)
registry.register(event_dates_dialog)

