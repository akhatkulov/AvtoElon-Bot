from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.alch import create_user,put_step
from loader import dp,bot

from keyboards.inline.user import home_menu,ads_yes_no


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    create_user(cid=message.chat.id)
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=home_menu())

@dp.callback_query_handler(lambda call: True)
async def get_ads(call: types.CallbackQuery):
    print(call)
    if call.data == "put_ads":
        print("-----")
        await bot.send_message(chat_id=call.message.chat.id, text="E'lon joylamoqchimisiz?", reply_markup=ads_yes_no())
    elif call.data == "yes_ads":
        await bot.send_message(chat_id=call.message.chat.id, text="Mashinaning 4ta rasmini yuboring")
        await put_step(cid=call.message.chat.id, step="get_photos")
    