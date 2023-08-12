from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Loader import categories, categories_transcription, modules, module_transcriptions

exit_button = InlineKeyboardButton(text="Закончить переписку", callback_data="Exit")

def makeKeyboard(buttonsContent: list(())):
    keyboard = InlineKeyboardMarkup(row_width=3)
    for buttonContent in buttonsContent:
        keyboard.add(InlineKeyboardButton(text=buttonContent[0], callback_data=buttonContent[1]))
    return keyboard.add(exit_button)



categoryChoiceButtons = [("Решить мою проблему", "SolveTheProblem"), ("Изучить продукты МТС", "LearnAboutMTSProducts")]

def makeModuleKeyboard():
    button1 = InlineKeyboardButton(text="Контроль перемещений", callback_data="Module")
    button2 = InlineKeyboardButton(text="Сообщения", callback_data="Messages")
    return InlineKeyboardMarkup(row_width=2).add(button1, button2, exit_button)

categoryChoiceKeyboard = makeKeyboard(categoryChoiceButtons)
productCategoryChoiceKeyboard = makeKeyboard(categories)
moduleKeyboard = makeKeyboard(modules)

