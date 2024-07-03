from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/habar", description="Adminga habar yuborish"),
        BotCommand(command="/admin", description="Admin bo'limi"),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
