from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Configs import bot_token
import json

bot = Bot(token=bot_token)
ms = MemoryStorage()

categories = []
categories_transcription = {}
modules = {}
module_transcriptions = {}

with open("Files/Services.json", encoding='utf-8') as f:
    file_data = json.loads(f.read())
    for key in file_data:
        categories.append(key)
        categories_transcription[key] = file_data[key]['transcription']
        for module in file_data[key]['modules']:
            if key in modules.keys():
                modules[key].extend([module])
            else:
                modules[key] = [module]

            module_transcriptions[module] = file_data[key]["modules"][module]['transcription']
