from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, inline_keyboard_button, \
    InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "мем 2017 года"), KeyboardButton(text = 'мем 2018 года'), KeyboardButton(text = 'мем 2019 года')],
                                     [KeyboardButton(text = 'рейд')]], resize_keyboard=True, input_field_placeholder="Выберите опцию")

mem_2017 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'Диана Шурыгина', callback_data='Diana_sh'),
                                                  InlineKeyboardButton(text = 'Сергей Дружко', callback_data='Sergey_dr')]])



get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'кинь номерок', request_contact=True)]], resize_keyboard=True)