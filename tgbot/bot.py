import asyncio
from aiogram import Bot, Dispatcher
from handlers import command_handlers
from keyboards.set_menu import set_main_menu
from configs.configs import load_config
from aiogram.fsm.storage.redis import RedisStorage
from aioredis.client import Redis

from tgbot.handlers import query_handlers


async def main() -> None:
    redis: Redis = Redis(host='localhost',port=6379)
    storage: RedisStorage = RedisStorage(redis=redis)
    config = load_config('.env')
    bot: Bot = Bot(token=config.token, parse_mode='HTML')

    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_router(command_handlers.router)
    dp.include_router(query_handlers.router)
    # dp.include_router(send_question_handler.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())