from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

MENU_TEXT_TEST_GENERATE = 'Test generatsiya qilish'
MENU_TEXT_TEST_RESULT = 'Test tekshirish'

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=MENU_TEXT_TEST_GENERATE),
            KeyboardButton(text=MENU_TEXT_TEST_RESULT),
        ],
    ],
    resize_keyboard=True
)
