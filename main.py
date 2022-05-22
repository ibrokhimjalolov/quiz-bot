from aiogram import executor
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.utils.db_api.django_db_api.config.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from loader import dp  # noqa
from bot.utils import on_startup_notify  # noqa
from bot.utils.set_bot_commands import set_default_commands  # noqa
from bot import filters, handlers, utils, data, states, keyboards, middlewares  # noqa


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
