import asyncio
import logging
import sys
from pathlib import Path

# Bot papkasini Python path ga qo'shish
BOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BOT_DIR))

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers import start, categories, projects, reviews, info

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(info.router)
    dp.include_router(categories.router)
    dp.include_router(projects.router)
    dp.include_router(reviews.router)

    logger.info("🤖 CODEFY APP bot ishga tushdi!")
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
