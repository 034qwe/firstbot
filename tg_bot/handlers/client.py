from re import search
from aiogram import Dispatcher,types
from create_bot import dp,bot
from keyboards import kb_client

#dp.message_handler(commands=['start'])
async def Hello_send(message: types.Message):
    await  bot.send_message(message.from_user.id,f'Hello {message.from_user.first_name}',reply_markup=(kb_client))


#@dp.message_handler(commands=['steam'])
async def my_steam(message: types.Message):
    await message.answer('my steam profile: https://steamcommunity.com/profiles/76561199154850620')


#@dp.message_handler(commands=['reverse'])
async def get_rvrs(message: types.Message):
    if message.text == '/reverse':
        await message.answer('write text after command please.')
    txt = message.text.replace('/reverse','')
    await message.answer(txt[::-1]) 


async def get_trnslt(message: types.Message):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    if message.text == '/translation':
        await message.answer('write text after command please.')
    txt = message.text.lower()
    txt = txt.replace('/translation','')
    a = ''  
    for i in txt:
        if i in t.keys():   
            a +=t[i]
        elif i == ' ':
            a+=' '
        else: 
            a+=str(i)
    await message.answer(a)


async def get_help(message: types.Message):
    await message.answer('My command: /translation, /start,/steam,/reverse,/search.\nOnly admin command:/moderator,/add_admin\nAlso i have a chat filter')

async def wikipedia(message: types.Message):
    if message.text == '/search':
        await message.answer('write what you want to find after the command')

    else:
        search_txt = message.text.replace('/search','').replace('\n','').replace(' ','')
        await message.answer(f'I managed to find: https://ru.wikipedia.org/wiki/{search_txt}') 



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(get_help,commands=['help'])
    dp.register_message_handler(get_trnslt,commands=['translation'])
    dp.register_message_handler(Hello_send,commands=['start'])
    dp.register_message_handler(my_steam,commands=['steam'])
    dp.register_message_handler(get_rvrs,commands=['reverse'])
    dp.register_message_handler(wikipedia,commands=['search'])