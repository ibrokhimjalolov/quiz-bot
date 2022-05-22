from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

from bot.data.config import ADMINS



class IsAdmin(BoundFilter):

    def check(self, message: Message) -> bool:
        return message.from_user.id in ADMINS
