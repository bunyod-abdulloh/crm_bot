from aiogram import Router, types, F
from aiogram.filters import CommandStart
from bot.loader import db

from bot.keyboards.reply.users_dkb import users_main_dkb

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):

    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username

    try:
        await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        pass
    await message.answer(
        text=f"Assalomu alaykum {full_name}!", reply_markup=users_main_dkb
    )


@router.message(F.text == "🏡 Bosh sahifa")
async def go_to_main_menu(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=users_main_dkb
    )
