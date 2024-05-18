import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
load_dotenv()
# TOKEN = os.getenv('BOT_TOKEN')
# bot = Bot(token=TOKEN)



async def main():
    print("Ish")
    from handlers import dp,bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
