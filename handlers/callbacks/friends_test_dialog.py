import operator

from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Multiselect, Column, Row, Group, Cancel
from aiogram_dialog.widgets.text import Const, Format

from main import dp
from loader import registry


class FriendsStates(StatesGroup):
    main = State()


# friends_kb_group = Group(
#     Button(Const("Иля 🧙‍♂"), id="ily"),
#     Button(Const("Кирилл 🕵️"), id="kirill"),
#     Button(Const("Потап 👨‍🏭"), id="potap"),
#     Button(Const("Лёха 👨‍🌾"), id="leha"),
#     Button(Const("Диман 🧑‍🍳"), id="diman"),
#     Button(Const("Паша 🧟‍♂️"), id="pasha"),
#     Button(Const("Лёня 👷🏻‍♂️"), id="lenya"),
#     Button(Const("Варя 🧝‍♀️"), id="varya"),
#     Button(Const("Рита 👰‍♀️"), id="rita"),
#     width=3
# )


# Getter для клавиатуры "friends"
async def get_friends(**kwargs) -> dict:
    friends = [("Иля 🧙‍♂", "Иля"),
               ("Кирилл 🕵️", "Кирилл"),
               ("Потап 👨‍🏭", "Потап"),
               ("Лёха 👨‍🌾", "Лёха"),
               ("Диман 🧑‍🍳", "Диман"),
               ("Паша 🧟‍♂️", "Паша"),
               ("Лёня 👷🏻‍♂️", "Лёня"),
               ("Атолл️ 💂‍♂️", "Атолл"),
               ("Рита 👰‍♀️", "Рита"),
               ("Варя 🧝‍♀️", "Варя"),
               ("Мари 🙇‍♀️", "Мари"),
               ("Настя 🧚‍♀️️", "Настя"),
               ]

    out_dict = {
        "friends": friends,
        "count": len(friends)
    }

    return out_dict

# Friends Keyboard
friends_kbd = Multiselect(
    checked_text=Format("✓ {item[0]}"),
    unchecked_text=Format("{item[0]}"),
    id="multi_friends",
    item_id_getter=operator.itemgetter(1),
    items="friends"
)


# A func to get the data from multiselect widget (testing how to get data)
async def retrieve_friends_data(message: types.Message, button: Button, dialog_manager: DialogManager) -> None:
    widget = dialog_manager.dialog().find("multi_friends")
    data = widget.get_checked()
    print(data)


# Second (bottom) friends keyboard - to change scenario (state, step)
friends_next_kb = Group(
    Button(
        Const("Some others"),
        id="friends_others",
        # on_click=
    ),
    Button(
        Const("That's all"),
        id="friends_end",
        on_click=retrieve_friends_data
    )
)

# The friends window
friends_window = Window(
    Const("Who was with us?"),
    Group(
        friends_kbd,
        friends_next_kb,
        width=3
    ),
    Cancel(Const("Cancel")),
    getter=get_friends,
    state=FriendsStates.main
)

# Creating and registration of the dialog
friends_dialog = Dialog(friends_window)
registry.register(friends_dialog)


# A func to start a "friends" dialog
@dp.message_handler(commands="friends")
async def friends_cmd(message: types.Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=FriendsStates.main, mode=StartMode.RESET_STACK)
