import logging
from aiogram import Dispatcher

from bot.data.config import DEVELOPERS


async def on_startup_notify(dp: Dispatcher):
    for user in DEVELOPERS:
        try:
            await dp.bot.send_message(user, "Bot started!")

        except Exception as err:
            logging.exception(err)
