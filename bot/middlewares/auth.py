from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.utils.db_api.django_db_api.core.models import TelegramUser


class AuthMiddleware(BaseMiddleware):
    """
    Simple middleware
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_process_message(self, message: types.Message, data: dict):
        TelegramUser.objects.create(
            id=message.from_user.id
        )
