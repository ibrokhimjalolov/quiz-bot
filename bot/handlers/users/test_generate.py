from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from bot.keyboards.default import MENU_TEXT_TEST_GENERATE
from bot.utils.service import TestGenerator


@dp.message_handler(text=MENU_TEXT_TEST_GENERATE)
async def test_generate(message: types.Message):
    file_path = TestGenerator(message.from_user.id).get_generated_file_path()
    file = open(file_path, 'rb')
    await message.answer_document(
        file
    )
