from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode, ChatEvent
from aiogram_dialog.widgets.kbd import Button, Checkbox, ManagedCheckboxAdapter
from aiogram_dialog.widgets.text import Const, Format

from main import dp
from loader import registry


class DialogStates(StatesGroup):
    main = State()


class SelectorStates(StatesGroup):
    selector_main = State()


# BEGINNING: Test command for HOMO///
main_window = Window(
    Const("Homo or no homo?"),
    Button(Const("HOMO!"), id="gay"),
    state=DialogStates.main
)

dialog = Dialog(main_window)
registry.register(dialog)


@dp.message_handler(commands="homo")
async def gay_command(message: types.Message, dialog_manager: DialogManager) -> None:
    print('homo is printing')
    await dialog_manager.start(state=DialogStates.main, mode=StartMode.RESET_STACK)
# END: Test command for HOMO ///


# Making a test Checkbox

async def check_changed(event: ChatEvent, checkbox: ManagedCheckboxAdapter, manager: DialogManager):
    print("test changed:", checkbox.is_checked())


check = Checkbox(
    Const("✓  Checked"),
    Const("X Unchecked"),
    id="check",
    on_state_changed=check_changed
)

check_window = Window(
    Const("Got your place. Who is with us today?"),
    check,
    state=SelectorStates.selector_main
)

check_dialog = Dialog(check_window)
registry.register(check_dialog)


@dp.message_handler(commands="test")
async def friends_kb(message: types.Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=SelectorStates.selector_main, mode=StartMode.RESET_STACK)
