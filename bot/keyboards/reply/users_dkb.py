from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

users_main_dkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍 Mahsulotlar')
        ],
        [
            KeyboardButton(text='👤 Shaxsiy kabinet'),
            KeyboardButton(text='🛒 Savat')
        ]
    ],
    resize_keyboard=True
)
