from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '8118742897:AAFJFwUMg6DfM6zlOmYVokhefoYg0lKe4H0'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands="start"))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)