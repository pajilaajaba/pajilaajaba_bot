import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

TOKEN = "7978725988:AAFjPWps0rk-Lt9tMGylqfJgqtUTuC-ltpQ"
MESSAGE_1 = "братик {} как двигаешься?"


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt():
        print('бот выключен')