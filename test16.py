from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '8118742897:AAFJFwUMg6DfM6zlOmYVokhefoYg0lKe4H0'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def my_start_filter(message: Message) -> bool:
    return message.text == '/start'

def custom_filter(some_list: list) -> bool:
    return sum([i for i in some_list if type(i) is int and i%7 == 0]) <= 83



# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')

@dp.message(custom_filter)
async def process_some_command(message: Message):
    await message.answer(text='Это команда custom_filter')


if __name__ == '__main__':
    dp.run_polling(bot)