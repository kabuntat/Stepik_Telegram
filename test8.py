import aiosqlite
import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

dp = Dispatcher()
bot = Bot("8118742897:AAFJFwUMg6DfM6zlOmYVokhefoYg0lKe4H0")

async def add_user(user_id, full_name, username):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    check_user = await check_user.fetchone()
    if check_user is None:
        await cursor.execute('INSERT INTO users (user_id, full_name, username) VALUES (?, ?, ?)',
                             (user_id, full_name, username))
        await connect.commit()
    else:
        print("уже есть")
    await cursor.close()
    await connect.close()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.answer("Welcome!")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

