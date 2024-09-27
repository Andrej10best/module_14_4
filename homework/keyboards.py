from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
).row(KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация'))


inline_kb = InlineKeyboardMarkup()
inline_b1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_b2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(inline_b1, inline_b2)


inline_kb_product = InlineKeyboardMarkup()
inline_b1 = InlineKeyboardButton(text='Витамин А', callback_data="product_buying")
inline_b2 = InlineKeyboardButton(text='Витамин В', callback_data="product_buying")
inline_b3 = InlineKeyboardButton(text='Витамин С', callback_data="product_buying")
inline_b4 = InlineKeyboardButton(text='Витамин D', callback_data="product_buying")
inline_kb_product.add(inline_b1, inline_b2, inline_b3, inline_b4)