from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Loader import categories, categories_transcription, modules, module_transcriptions

back_button = InlineKeyboardButton(text="Вернуться в начало", callback_data="BackToMenu")
exit_button = InlineKeyboardButton(text="Закончить переписку", callback_data="Exit")

def makeKeyboard(buttonsContent: list()):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for buttonContent in buttonsContent:
        keyboard.insert(InlineKeyboardButton(text=buttonContent[0], callback_data=buttonContent[1]))
    return keyboard.add(back_button, exit_button)

categoryChoiceButtons = [("Решить мою проблему", "РешитьПроблему"), ("Изучить продукты МТС", "ИзучитьПродукт"), ("Подобрать услугу", "ПодобратьУслугу")]
answerButtons = [("Да", "Yes"), ("Нет", "No")]

standartKeyboard = makeKeyboard([])
answerKeyboard =  makeKeyboard(answerButtons)
categoryChoiceKeyboard = makeKeyboard(categoryChoiceButtons)
productCategoryChoiceKeyboard = makeKeyboard(categories)
modules_keyboard = {}
for module in modules:
    modules_keyboard[module] = makeKeyboard(modules[module])

