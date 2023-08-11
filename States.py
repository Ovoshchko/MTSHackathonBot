from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    ChoiceState = State()
    ProductState = State()
    ProblemsState = State()
