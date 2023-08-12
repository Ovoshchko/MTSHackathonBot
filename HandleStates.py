from States import States
from aiogram import types
from aiogram import Dispatcher
from Loader import bot, ms
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.state import State
from Keyboards import categoryChoiceKeyboard, productCategoryChoiceKeyboard, makeModuleKeyboard
from aiogram.dispatcher.filters import Command

dp = Dispatcher(bot=bot, storage=ms)


async def suggestModules(call: CallbackQuery):
    await call.message.answer("Вы можете позникомиться ближе с услугами, выбрав соответствующий модуль.", reply_markup=makeModuleKeyboard())

@dp.message_handler(Command('start'), state="*")
async def startCommand(message: types.Message):
    await message.answer("Добрый день для вас и хороший для бизнеса. Я ваш персональный ассисент Мтси. Чем я могу вам помочь?", reply_markup=categoryChoiceKeyboard)
    await State.set(States.ChoiceState)

@dp.callback_query_handler(text=['SolveTheProblem'], state=States.ChoiceState)
async def startProblemSolution(call: CallbackQuery):
    await call.message.answer("Опишите вашу проблему:")
    await State.set(States.ProblemsState)

@dp.callback_query_handler(text=['LearnAboutMTSProducts'], state=States.ChoiceState)
async def showProducts(call: CallbackQuery):
    await call.message.answer("Выберите категорию", reply_markup=productCategoryChoiceKeyboard)
    await State.set(States.ProductState)

@dp.callback_query_handler(text=["Employee"], state=States.ProductState)
async def showEmployeeService(call: CallbackQuery):
    await call.message.answer(call.message)
    await suggestModules(call)


@dp.callback_query_handler(text=["Exit"], state="*")
async def exit(call: CallbackQuery):
    await call.message.answer("Надеюсь, я смог вам помочь. Не бойтесь обращаться ко мне за помощью, я постараюсь вам помощь в решении ваших проблем;)")


@dp.message_handler(state="*")
async def other(message: types.Message):
    await message.answer("NONOONNO")
