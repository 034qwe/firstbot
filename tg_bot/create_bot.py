from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage= MemoryStorage()
TOKEN = '5760311576:AAHKUdzcEhD1vyAVw_KEdiB_NGmukDhXQ2k'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=storage)