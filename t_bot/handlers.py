from aiogram import Dispatcher, types,F
from aiogram.filters import CommandStart
dp = Dispatcher()
from keyboards import apple_kb

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=apple_kb)

@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: types.Message):
    await msg.answer(msg.web_app_data.data)





