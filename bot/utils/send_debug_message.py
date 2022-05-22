import logging

from bot.data.config import ADMINS, DEVELOPERS

from loader import dp



async def message2admins(text):
    for user in ADMINS:
        try:
            await dp.bot.send_message(user, text)
        except Exception as err:
            logging.exception(err)


async def message2devs(text):
    for user in DEVELOPERS:
        try:
            await dp.bot.send_message(user, text)
        except Exception as err:
            logging.exception(err)
