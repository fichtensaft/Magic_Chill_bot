import operator

from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Multiselect
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

async def get_friends(**kwargs) -> dict:
    friends = ["Иля 🧙‍♂",
               "Кирилл 🕵️",
               "Потап 👨‍🏭",
               "Лёха 👨‍🌾",
               ]

    out_dict = {
        "friends": friends,
        "count": len(friends)
    }

    print(out_dict)
    return out_dict


friends_list = [("Иля 🧙‍♂", 1),
                ("Кирилл 🕵️", 2),
                ("Потап 👨‍🏭", 3),
                ("Лёха 👨‍🌾", 4)
                ]

friends_kbd = Multiselect(
    checked_text=Format("✓ {item[0]}"),
    unchecked_text=Format("{item[0]}"),
    id="m_friends",
    item_id_getter=operator.itemgetter(0),
    items=friends_list
)

friends_window = Window(
    Const("Who was with us?"),
    friends_kbd,
    state=FriendsStates.main
)

friends_dialog = Dialog(friends_window)
registry.register(friends_dialog)


@dp.message_handler(commands="friends")
async def friends_cmd(message: types.Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=FriendsStates.main, mode=StartMode.RESET_STACK)
