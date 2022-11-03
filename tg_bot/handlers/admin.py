from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp,bot
from aiogram import types,Dispatcher
from data1 import sqlite1
from keyboards.admin_kb import kb_admin


ID = 5512193079



async def send_kb(message:types.Message):
    if message.from_user.id in await sqlite1.id_admin():
        await bot.send_message(message.from_user.id,'keyboard send',reply_markup=(kb_admin))

async def add_admin(message:types.Message):
        if message.text == '/add_admin':
            await message.answer('Enter id a new admin after command')     
        
        elif  message.from_user.id == ID:
            if ID not in [i for i in sqlite1.id_admin()]:
                sqlite1.sql_add2(ID)
                
            
            txt = message.text.replace('/add_admin','').replace(' ','').replace('\n','')
            await sqlite1.sql_add2(txt)
            await message.answer('id added in database')

        else:
            await message.answer('you not main admin')    


class FSMadmin(StatesGroup):
    photo = State()
    name  = State()
    category = State()
 

async def  cm_start(message:types.Message):
    if message.from_user.id in await sqlite1.id_admin():
        await FSMadmin.photo.set()
        await message.reply('download photo pls')


async def load_photo(message:types.Message,state:FSMContext):
    if message.from_user.id in await sqlite1.id_admin():
        async with  state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next() 
        await message.reply('Name hero pls')


async def load_name(message:types.Message,state:FSMContext):
    if message.from_user.id in await sqlite1.id_admin():
        async with  state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.reply('enter category hero...')


async def  load_category(message:types.Message,state:FSMContext):
    if message.from_user.id in await sqlite1.id_admin():
        async with  state.proxy() as data:
            data['category'] = message.text

        await sqlite1.sql_add(state)

        await state.finish()


async def exit_handler(message: types.Message,state:FSMContext):
    _state_ = await state.get_state()
    if _state_ is None:
        return
    await state.finish()
    await message.reply('ok')


def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start,commands=['load'])
    dp.register_message_handler(load_photo,content_types=['photo'],state=FSMadmin.photo)
    dp.register_message_handler(load_name,state=FSMadmin.name)
    dp.register_message_handler(load_category,state=FSMadmin.category)
    dp.register_message_handler(send_kb,commands=['moderator'])
    dp.register_message_handler(exit_handler,commands=['exit'],state="*")
    dp.register_message_handler(add_admin,commands=['add_admin'])