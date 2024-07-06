from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.alch import create_user,put_step
from loader import dp,bot

from keyboards.inline.user import home_menu,ads_yes_no


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    create_user(cid=message.chat.id)
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=home_menu())
