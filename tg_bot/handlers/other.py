from aiogram import Dispatcher,types
from create_bot import dp


async def filter_txt(message: types.Message):
    file = open("tg_bot/bed_words.txt",encoding='utf-8')
    check_lst = [i for i in file.read().split()]
    for word in message.text.split():
        if word.lower() in check_lst:
            await message.delete()
            await message.answer("don't worry")
    file.close()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(filter_txt)