from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

bd1 = KeyboardButton('/load')
bd2 = KeyboardButton('/add_admin')

kb_admin = ReplyKeyboardMarkup(one_time_keyboard=True)

kb_admin.add(bd1,bd2)