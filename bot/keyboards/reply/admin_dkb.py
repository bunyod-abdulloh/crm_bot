from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_main_dkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔍 Skaner")
        ],
        [
            KeyboardButton(text="🌐 Web admin panel")
        ],
        [
            KeyboardButton(text="😎 Foydalanuvchilar bo'limi")
        ],
        [
            KeyboardButton(text="🏡 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)