from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp
from bot.keyboards.default import MENU_TEXT_TEST_RESULT
from bot.states.main import GlobalState
from bot.utils.service import TestChecker


@dp.message_handler(text=MENU_TEXT_TEST_RESULT)
async def test_result_entry(message: types.Message):
    await GlobalState.test_result.set()
    await message.answer(
        "Javoblarni kiriting:\n Namuna: 123: abcdaabcdaabcdaabcdaabcdaabcdaabcda"
    )


@dp.message_handler(state=GlobalState.test_result)
async def test_result_entry(message: types.Message, state: FSMContext):
    await state.finish()
    checker = TestChecker(message.text, message.from_user.id).get_score()
    if checker != -1:
        await message.answer(
            "Natijangiz: " + str(checker)
        )
    else:
        await message.answer(
            "Noto'gri format yoki xato kod"
        )

