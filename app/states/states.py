from aiogram.fsm.state import State, StatesGroup

class Get_channel(StatesGroup):
    get_channel = State()

class Get_post(StatesGroup):
    get_post = State()
    get_button_text = State()
    get_button_url = State()
    check = State()