from aiogram import Bot, Dispatcher, F
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


@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)
    await message.answer("photo")

@dp.message(F.audio)
async def send_audio_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_audio(message.audio.file_id)
    await message.answer("audio")

@dp.message(F.video)
async def send_video_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_video(message.video.file_id)
    await message.answer("video")

@dp.message(F.sticker)
async def send_video_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_sticker(message.sticker.file_id)
    await message.answer("sticker")

@dp.message(F.animation)
async def send_video_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_animation(message.animation.file_id)
    await message.answer("animation")

#
@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    try:
        await message.reply(message.text)
        await message.answer("text")
    except:
        await message.answer("Content type error")



if __name__ == '__main__':
    dp.run_polling(bot)