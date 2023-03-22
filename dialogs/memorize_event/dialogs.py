import operator

from aiogram.types import ContentType

from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, Column, Group, Select, Multiselect
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import MessageInput, TextInput

from loader import registry
from dialogs.states import MemorizeEvent
from dialogs.memorize_event import getters
from dialogs.memorize_event import handlers


# Creating a 'Memorize_Event Dialog' and its Windows, etc.
"""
Window for the 'Date' part of Memo-dialog
"""
date_window = Window(
    Const("When was the day?"),
    Column(
        Button(
            Format("Today - {date_today}?"),
            id="is_today",
            on_click=handlers.date_to_places
        ),
        Button(
            Const("Another day"),
            id="not_today",
            on_click=handlers.next_state
        ),
        Button(
            Const("Stop memorizing"),
            id="date_cancel_but",
            on_click=handlers.date_dialog_done
        )
    ),
    getter=getters.date_getter,
    state=MemorizeEvent.date
)

"""
Window for the inputting your own date 
"""
date_input_window = Window(
    Const("Enter the date in the format - 'day month year' (separated by spaces):"),
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
    Const("Where were we?"),
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
    Const("Then where were you? Enter the place, pretty please:"),
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
    Const("Who were there in such a magical day?"),
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
    Const("Who else? Enter their names separated by ';', lad:"),
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
    Const("What's with your head, choom?"),
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
Creating the Memes part of Memo-dialog
"""
memes_window = Window(
    Const("Что по кекам?\n(каждый кек с новой строки, на конце , или ;)"),
    TextInput(
        id="memes_input_text",
        type_factory=str,
        on_success=handlers.memes_success
    ),
    state=MemorizeEvent.memes
)

"""
Creating the part where we ask user if he wants to send a Photo of Memo-dialog
"""
photos_window = Window(
    Const("By the way\n"
          "Do you want to pin some photos to the event?"),
    Column(
        Button(
            Const("Yep 📸"),
            id="photos_yes_but",
            on_click=handlers.next_state
        ),
        Button(
            Const("Nah 🗿"),
            id="photos_no_but",
            on_click=handlers.memorizing_photo_no
        ),

    ),
    state=MemorizeEvent.photos
)

"""
Creating the first-Photo-input part of Memo-dialog
"""
photos_input_window = Window(
    Const("Send only one photo that you want to pin to the event 🌄"
          "\nIf you want, you can send other photos one by one after that"),
    MessageInput(
        func=handlers.photos_input_got,
        content_types=ContentType.PHOTO
    ),
    state=MemorizeEvent.photos_input

)

"""
Creating the second-Photo-input part of Memo-dialog -> add more photos in memorizing-scenario
"""
more_photos_input_window = Window(
    Const("Send only one photo that you want to pin to the event 🌄"
          "\nIf you want, you can send other photos one by one after that"),
    MessageInput(
        func=handlers.input_more_photos,
        content_types=ContentType.PHOTO
    ),
    state=MemorizeEvent.add_more_photos

)


"""
Creating the last part - reusable  other photos-input part of Memo-dialog
"""
more_photos_window = Window(
    Const("One more photo? 📷"),
    Column(
        Button(
            Const("Yes, one more 🖼"),
            id="more_photo_yes_but",
            on_click=handlers.memorizing_more_photo_yes,
        ),
        Button(
            Const("No, that's all 🔚"),
            id="more_photo_no_but",
            on_click=handlers.memorizing_more_photo_no,
        )
    ),
    state=MemorizeEvent.ask_more_photos
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
    memes_window,

    photos_window,
    photos_input_window,
    more_photos_window,
    more_photos_input_window
]
memorize_dialog = Dialog(*memorize_windows)
registry.register(memorize_dialog)
