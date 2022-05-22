from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from bot.keyboards.default import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Salom, {message.from_user.full_name}!",
        reply_markup=menu
    )
