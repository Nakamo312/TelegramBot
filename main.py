
from aiogram import Bot, Router, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from configs import APITOKEN

import asyncio
bot = Bot(token=APITOKEN)

user_private = Router()

@user_private.message(CommandStart())
async def hello_world(message: types.Message):
    await message.answer("Привет! Я бот с рассписанием!")


dp = Dispatcher()

dp.include_router(user_private)

async def main():
    await dp.start_polling(bot)


asyncio.run(main())