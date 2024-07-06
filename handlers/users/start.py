from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.alch import create_user
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await create_user(cid=message.chat.id)