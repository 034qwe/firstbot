from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove



b1 = KeyboardButton('/start')
b2 = KeyboardButton('/steam')
b3 = KeyboardButton('/help')
b4 = KeyboardButton('my phone number',request_contact=True)
b5 = KeyboardButton('My geolocation',request_location=True)



kb_client = ReplyKeyboardMarkup(one_time_keyboard=True)
kb_client.row(b1,b2,b3).add(b4).add(b5)