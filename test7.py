import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

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

@dp.callback_query(F.data == "menu")
async def menu_callback(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Оставить заявку", callback_data='request_for_connection'),
         types.InlineKeyboardButton(text="Задать вопрос", callback_data='question')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f"Мы рады приветствовать Вас, {callback.from_user.full_name}! Если Вы хотите оставить заявку на подключение, или у Вас есть вопрос по действующей услуге - выберите соответствующий пункт меню:", reply_markup=keyboard)

@dp.callback_query(F.data == "request_for_connection")
async def request_for_connection_handler(callback: types.CallbackQuery):
    kb = [
        [
            types.InlineKeyboardButton(text="Вернуться", callback_data='menu')
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('Благодарим за выбор нашей компании! Для оформления заявки потребуются ваши данные.\n'
                         'Укажите, пожалуйста, ваши фамилию, имя и отчество.', reply_markup=keyboard)

@dp.callback_query(F.data == "question")
async def question_handler(callback: types.CallbackQuery):
    kb = [
        [
            types.InlineKeyboardButton(text="Вернуться", callback_data='menu')
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('Благодарим за обращение. Задайте интересующий Вас вопрос или опишите проблему. Мы свяжемся с Вами в ближайшее время и постараемся Вам помочь.', reply_markup=keyboard)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())