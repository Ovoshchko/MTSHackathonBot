from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Configs import bot_token
import json
from aiogram import Dispatcher

bot = Bot(token=bot_token)
ms = MemoryStorage()
dp = Dispatcher(bot=bot, storage=ms)

raw_categories = []
categories = []
categories_transcription = {}
raw_modules = []
modules = {}
module_transcriptions = {}

with open("Files/Services.json", encoding='utf-8') as f:
    file_data = json.loads(f.read())
    for key in file_data:
        callback_data = file_data[key]['callback_data']
        raw_categories.append(key)
        categories.append((key, callback_data))
        categories_transcription[callback_data] = file_data[key]['transcription']
        for module in file_data[key]['modules']:
            raw_modules.append(module)
            if key in modules.keys():
                modules[key].extend([(module, module)])
            else:
                modules[key] = [(module, module)]

            module_transcriptions[module] = file_data[key]["modules"][module]['transcription']

