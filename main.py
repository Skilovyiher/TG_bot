import asyncio
import logging

import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command

from handlers.media_handlers import router as media_router
from handlers.basic_handlers import router as basic_router
from handlers.menu_handlers import router as menu_router

logging.basicConfig(level=logging.INFO)

load_dotenv()

BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    
    dp.include_routers(menu_router, media_router, basic_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())