from aiogram import types
from loader import dp

from utils.db_api.alch import put_step
from keyboards.inline.user import ads_yes_no

@dp.callback_query_handler(text="put_ads")
async def uz_show_apps(call: types.CallbackQuery):
    await call.message.answer("E'lon joylamoqchimisiz?", reply_markup=ads_yes_no())
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yes_ads")
async def uz_show_apps(call: types.CallbackQuery):
    await call.message.answer("Mashinaning 4ta rasmini yuboring")
    put_step(cid=call.message.chat.id, step="get_photos")
    await call.answer(cache_time=60)