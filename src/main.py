import logging
import asyncio
import sys
from aiogram import Bot, Dispatcher
from config.config import settings
from handler.router import get_routers


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=settings.token)

    for router in get_routers():
        dp.include_router(router)


    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
