from aiogram.utils import executor
from create_bot import dp
from handlers import admin,client,other
from data1 import sqlite1


async def on_startup(_):
    print('bot start')
    sqlite1.data_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


    
executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
