from aiogram import Dispatcher, types
from aiogram.filters import CommandStart
dp = Dispatcher()
from keyboards import apple_kb

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=apple_kb)