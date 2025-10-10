import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject
from aiogram.filters import BaseFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

dp = Dispatcher()
bot = Bot("8118742897:AAFJFwUMg6DfM6zlOmYVokhefoYg0lKe4H0")
admin_ids = [422161988]

class IsAdmin(BaseFilter):
    async def __call__(self, obj: TelegramObject) -> bool:
        return obj.from_user.id in admin_ids

class AdminState(StatesGroup):
    newsletter = State()

async def add_user(user_id, full_name, username):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    check_user = await check_user.fetchone()
    if check_user is None:
        await cursor.execute('INSERT INTO users (user_id, full_name, username) VALUES (?, ?, ?)',
                             (user_id, full_name, username))
        print(f'New user: {check_user}')
        await connect.commit()
    else:
        print("уже есть")
    await cursor.close()
    await connect.close()

async def get_user_count():
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    user_count = await cursor.execute('SELECT COUNT(*) FROM users')
    user_count = await user_count.fetchone()
    await cursor.close()
    await connect.close()
    return user_count[0]

async def get_user_list():
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    users = await cursor.execute('SELECT * FROM users')
    users = await cursor.fetchall()
    await cursor.close()
    await connect.close()
    return users

async def get_all_user_id():
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    users = await cursor.execute('SELECT user_id FROM users')
    users = await cursor.fetchall()
    await cursor.close()
    await connect.close()
    users = [user[0] for user in users]
    return users

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.InlineKeyboardButton(text="Оставить заявку", callback_data='request_for_connection'),
         types.InlineKeyboardButton(text="Задать вопрос", callback_data='question')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.answer(f"Мы рады приветствовать Вас, {message.from_user.full_name}! "
                         f"Если Вы хотите оставить заявку на подключение, "
                         f"или у Вас есть вопрос по действующей услуге - выберите соответствующий пункт меню:", reply_markup=keyboard)


@dp.callback_query(F.data == "request_for_connection")
async def request_for_connection_handler(callback: types.CallbackQuery):
    await callback.message.answer('Благодарим за выбор нашей компании! Для оформления заявки потребуются ваши данные.\n'
                         'Укажите, пожалуйста, ваши фамилию, имя и отчество.')

@dp.callback_query(F.data == "question")
async def question_handler(callback: types.CallbackQuery):
    await callback.message.answer('Благодарим за обращение. Задайте интересующий Вас вопрос или опишите проблему. '
                                     'Мы свяжемся с Вами в ближайшее время и постараемся Вам помочь.')


@dp.message(Command('admin'), IsAdmin())
async def admin_command(message: types.Message) -> None:
    kb = [
        [types.InlineKeyboardButton(text="Статистика", callback_data='admin_statistic'),
         types.InlineKeyboardButton(text="Список пользователей", callback_data='user_list'),
         types.InlineKeyboardButton(text="Рассылка", callback_data='news')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Добро пожаловать в Админ-панель!', reply_markup=keyboard)

@dp.callback_query(F.data == "admin_statistic")
async def admin_stats_handler(callback: types.CallbackQuery):
    user_count = await get_user_count()
    await callback.message.answer(f'{user_count} уникальных пользователей')

@dp.callback_query(F.data == "user_list")
async def admin_users_handler(callback: types.CallbackQuery):
    user_list = await get_user_list()
    for user_tuple in user_list:
        user = tuple(map(str, user_tuple))
        await callback.message.answer("    ".join(user))

@dp.callback_query(F.data == "news")
async def admin_news_handler(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer('Введите сообщение для рассылки')
    await state.set_state(AdminState.newsletter)

@dp.message(AdminState.newsletter)
async def admin_news_message(message: types.Message, state: FSMContext, bot: Bot):
    msg = message.text
    users = await get_all_user_id()
    i = 0
    for user in users:
        try:
            await bot.send_message(user, msg)
            await asyncio.sleep(0.1)
            i += 1
        except:
            pass
    await message.answer(f'✅Рассылка завершена. Отправлено сообщений: {i}')
    await state.clear()



async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

