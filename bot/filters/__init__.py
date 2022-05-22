from loader import dp

from .admin import IsAdmin
from .chat_type import (
    IsChannelChat,
    IsGroupChat,
    IsPrivateChat
)

if __name__ == "bot.filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsChannelChat)
    dp.filters_factory.bind(IsGroupChat)
    dp.filters_factory.bind(IsPrivateChat)
