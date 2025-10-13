import asyncio

from aiogram import Dispatcher, types, Bot

dp = Dispatcher()

@dp.message()

async def hello(message: types.Message):
    await message.send_copy(message.from_user.id)

async def main():
    bot = Bot(token='8118742897:AAFJFwUMg6DfM6zlOmYVokhefoYg0lKe4H0')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
