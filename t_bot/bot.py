import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
load_dotenv()
# TOKEN = os.getenv('BOT_TOKEN')
# bot = Bot(token=TOKEN)

dp = Dispatcher()

#
# @dp.message(CommandStart())
# async def cmd_start(message: types.Message):
#     await message.answer("Assalomu Aleykum!\n Do'konimizga xush kelibsiz!")

async def main():
    print("Ish")
    from handlers import dp,bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
