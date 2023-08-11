from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Configs import bot_token

bot = Bot(token=bot_token)
ms = MemoryStorage()

categories = [("Сотрудники", "Employee"), ("Транспорт", "Transport")]