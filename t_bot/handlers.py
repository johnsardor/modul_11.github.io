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
    product_data = text.split("|")
    products = {}
    for i in range(len(product_data)):
        if len(product_data[i].split("/")) >= 3:
            title = product_data[i].split('/')[0]
            price = product_data[i].split('/')[1]
            quantity = int(product_data[i].split('/')[2])
            product = {
                "Nomi": title,
                "Price": int(price),
                "Quantity": int(quantity)
            }
            products[i] = product
    await bot.send_invoice(
        chat_id=msg.chat.id,
        title="To'lov",
        description="Telegram bot orqali to'lov!",
        provider_token=Provider_token,
        currency="UZS",
        payload="Ichki malumot",
        prices=[LabeledPrice(
            label=f"{product['Nomi']} ({product['Quantity']})",
            amount=product["Price"] * product["Quantity"] * 100
        ) for product in products.values()]
    ),
