from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    OptionsChoiceState = State()
    ProductChoiceState = State()
    ModuleChoiceState = State()
    ProblemSolvingState = State()

