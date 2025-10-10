from aiogram import types, Dispatcher
from aiogram.filters import CommandStart
import html


async def start_command(message: types.Message):
    await message.answer(f'<b>{html.escape(message.from_user.full_name)},</b> привет!\n\n'
                         f'Бот загадал число от 1 до 10, попробуй отгадать.')


def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
