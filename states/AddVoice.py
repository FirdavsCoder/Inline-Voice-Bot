from aiogram.dispatcher.filters.state import State, StatesGroup

class AddVoiceState(StatesGroup):
    audio = State()
    name = State()