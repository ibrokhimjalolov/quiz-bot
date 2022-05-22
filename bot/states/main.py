from aiogram.dispatcher.filters.state import StatesGroup, State


class GlobalState(StatesGroup):
    test_generate = State()
    test_result = State()
