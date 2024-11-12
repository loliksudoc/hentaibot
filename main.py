from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command

API_TOKEN = '7745141185:AAH4t7gLib4G2GnQVc16vFn8twMPfNI_K9s'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Пример исправленной публичной ссылки
catalog_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Жестокий', url='https://t.me/+ugzSHlpsWkcxYjQ6')],  # Замените на правильную ссылку
        [InlineKeyboardButton(text='от первого лица', url='https://t.me/+R3fBROHv3Tk3Mzky')],
        [InlineKeyboardButton(text='Милфы', url='https://t.me/+N2yZFSbD4R4xOWQ6')]
    ],
    row_width=2
)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    photo_url = 'https://avatars.mds.yandex.net/get-games/11385414/2a0000018d3d599d89aea6822e75e16437af/orig'
    await message.answer_photo(photo=photo_url, caption='привет дорогой пользаватель бота! мы проект который дает классные Аниме(не очень хорошего содержание🥵) БЕЗ ОБМАНА☃️')
    await message.reply('Выбери команду для продолжение💫 /hentai /creator')

@dp.message(Command('hentai'))
async def cmd_help(message: Message):
    await message.reply('Выберите жанр хентайчика', reply_markup=catalog_list)

@dp.message(Command('creator'))
async def cmd_help(message: Message):
    await message.reply('Создатель данного бота дрочун @zxclolik')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
     asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
