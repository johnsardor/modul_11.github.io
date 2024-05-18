import os
from aiogram import Dispatcher, F, Bot,types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery

from dotenv import load_dotenv

from keyboards import apple_kb
TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)

Provider_token = os.getenv("PROVIDER_TOKEN")

load_dotenv()


dp = Dispatcher()


@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Salom", reply_markup=apple_kb)


@dp.message(Command("pay"))
async def order(msg: Message):
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="Telegram bot orqali to'lov!",
        description="Telegram bot orqali to'lov qilishni o'rganyammiz!",
        provider_token=Provider_token,
        currency="uzs",
        payload="Ichki malumot",  # Foydalanuvchiga ko'rinmiydi
        prices=[
            LabeledPrice(label="TOVAR", amount=2000000),
            LabeledPrice(label="TOVAR", amount=1000000)
        ]
    )


async def pre_checkout(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)



@dp.message(F.func(lambda msg: msg.web_app_data.data))
async def get_btn(msg: Message):
    text = msg.web_app_data.data
    products = text.split("|")
    summa = 0
    for i in range(len(products)):
        if len(products[i].split("/")) >= 3:
            title = products[i].split('/')[0]
            price = int(products[i].split('/')[1])
            quantity = int(products[i].split('/')[2])
            await msg.answer(text=f"Nomi: {title}\n"
                                  f"Narxi: {price}\n"
                                  f"Soni: {quantity}\n"
                                  f"Umumiy narxi: {quantity * price}$")
            summa += price * quantity
    await msg.answer(text=f"To'lanishi kerak: {summa}$", reply_markup=apple_kb)
