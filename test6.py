import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from pyexpat.errors import messages

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
bot = Bot("8118742897:AAFJFwUMg6DfM6zlOmYVokhefoYg0lKe4H0")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.InlineKeyboardButton(text="Оставить заявку", callback_data='request_for_connection'), types.InlineKeyboardButton(text="Задать вопрос", callback_data='question')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(f"Мы рады приветствовать Вас, {message.from_user.full_name}! Если Вы хотите оставить заявку на подключение, или у Вас есть вопрос по действующей услуге - выберите соответствующий пункт меню:", reply_markup=keyboard)


@dp.callback_query(F.data == "request_for_connection")
async def request_for_connection_handler(callback: types.CallbackQuery):
    await callback.message.answer('Благодарим за выбор нашей компании! Для оформления заявки потребуются ваши данные.\n'
                         'Укажите, пожалуйста, ваши фамилию, имя и отчество.')
    @dp.message()
    async def hello(message: types.Message):
        print(message.text)
        await message.answer("Ваш контактный номер телефона?")

@dp.callback_query(F.data == "question")
async def question_handler(callback: types.CallbackQuery):
    await callback.message.answer('Благодарим за обращение. Задайте интересующий Вас вопрос или опишите проблему. Мы свяжемся с Вами в ближайшее время и постараемся Вам помочь.')

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())