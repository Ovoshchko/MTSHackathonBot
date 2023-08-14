from States import States
from aiogram import types
from Loader import dp
from Files.Texts import *
import random
from Loader import categories, categories_transcription, modules, module_transcriptions, raw_categories, raw_modules
from aiogram.types import CallbackQuery
from OpenAIConnector import getAnswerForQuestion, findSolutionFromMTS, unsuccess_answer
from aiogram.dispatcher.filters.state import State
from Keyboards import categoryChoiceKeyboard, productCategoryChoiceKeyboard, modules_keyboard, standartKeyboard
from aiogram.dispatcher.filters import Command

last_category = ""

@dp.message_handler(Command('start'), state="*")
async def startCommand(message: types.Message):
    await message.answer(random.choice(start_messages), reply_markup=categoryChoiceKeyboard)
    await State.set(States.OptionsChoiceState)

@dp.callback_query_handler(text=['РешитьПроблему'], state=States.OptionsChoiceState)
async def startProblemSolution(call: CallbackQuery):
    await call.message.answer(random.choice(problem_asking_messages), reply_markup=standartKeyboard)
    await State.set(States.ProblemSolvingState)

@dp.message_handler(state=States.ProblemSolvingState)
async def problemTaken(message: types.Message):
    answer = await getAnswerForQuestion(message.text)
    await message.answer(answer)
    if answer != unsuccess_answer:
        mts_service = await findSolutionFromMTS(message.text)
        await message.answer(mts_service)
        await message.answer(("Вы можете продолжить поиск решений или перейти в основное меню." 
                         "Я постараюсь помочь вам всем, чем смогу."), reply_markup=standartKeyboard)

@dp.callback_query_handler(text=['ИзучитьПродукт'], state=States.OptionsChoiceState)
async def showProducts(call: CallbackQuery):
    await call.message.answer("Выберите категорию", reply_markup=productCategoryChoiceKeyboard)
    await State.set(States.ProductChoiceState)

@dp.callback_query_handler(text=raw_categories, state=States.ProductChoiceState)
async def showCategory(call: CallbackQuery):
    await call.message.answer(categories_transcription[call.data]+"\nЗдесь представлены модули, входящие в состав сервиса "+call.data+".\nВыберите сервис, про который хотели бы узнать подробнее:", reply_markup=modules_keyboard[call.data])
    await State.set(States.ModuleChoiceState)
    global last_category
    last_category = call.data

@dp.callback_query_handler(text=raw_modules, state=States.ModuleChoiceState)
async def showModule(call: CallbackQuery):
    await call.message.answer(module_transcriptions[call.data])
    await call.message.answer("\nЗдесь представлены модули, входящие в состав сервиса "+call.data+".\n Выберите сервис, про который хотели бы узнать подробнее:", reply_markup=modules_keyboard[last_category])

@dp.callback_query_handler(text=["BackToMenu"], state="*")
async def back(call: CallbackQuery):
    await startCommand(call.message)

@dp.callback_query_handler(text=["Exit"], state="*")
async def exit(call: CallbackQuery):
    await call.message.answer("Надеюсь, я смог вам помочь. Не бойтесь обращаться ко мне за помощью, я постараюсь вам помощь в решении ваших проблем;)")


@dp.message_handler(state="*")
async def other(message: types.Message):
    await message.answer("NONOONNO")
