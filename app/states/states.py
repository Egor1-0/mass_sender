from aiogram.fsm.state import State, StatesGroup

class Сhannel(StatesGroup):
    get_channel_id = State()
    get_channel_name = State()


class Post(StatesGroup):
    get_post = State()
    get_button_text = State()
    get_button_url = State()
    check = State()