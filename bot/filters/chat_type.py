from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import BoundFilter



class IsPrivateChat(BoundFilter):

    async def check(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE



class IsGroupChat(BoundFilter):

    async def check(self, message: Message) -> bool:
        return message.chat.type in [
            ChatType.GROUP,
            ChatType.SUPER_GROUP,
        ]



class IsChannelChat(BoundFilter):

    async def check(self, message: Message) -> bool:
        return message.chat.type == ChatType.CHANNEL
