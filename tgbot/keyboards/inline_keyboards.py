from aiogram.types import InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from tgbot.lexicon.lixicon_ru import LEXICON_RU


def create_start_inline_keyboard():
    start_kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    start_send_cards_inline_button:InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['start_inline_buttons']['start_send_cards_inline_button'],
                callback_data='start_send_cards_inline_button')
    feedback_inline_button:InlineKeyboardButton = InlineKeyboardButton(
                    text=LEXICON_RU['start_inline_buttons']['send_feedback_inline_button'],
                    web_app=WebAppInfo(url=LEXICON_RU['links']['feedback']))
    quiz_inline_button:InlineKeyboardButton = InlineKeyboardButton(
                    text=LEXICON_RU['start_inline_buttons']['quiz_inline_button'],
                    web_app=WebAppInfo(url=LEXICON_RU['links']['quiz']))
    buttons: list[InlineKeyboardButton] = [quiz_inline_button,feedback_inline_button,start_send_cards_inline_button]
    start_kb_builder.row(*buttons, width=1)
    return start_kb_builder.as_markup()


def create_picture_inline_keyboard():
    picture_kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    start_send_cards_inline_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['picture_inline_buttons']['get_one_more_card'],
        callback_data='get_one_more_card')
    feedback_inline_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['picture_inline_buttons']['send_feedback_inline_button'],
        web_app=WebAppInfo(url=LEXICON_RU['links']['feedback']))
    quiz_inline_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['picture_inline_buttons']['quiz_inline_button'],
        web_app=WebAppInfo(url=LEXICON_RU['links']['quiz']))
    buttons: list[InlineKeyboardButton] = [quiz_inline_button, feedback_inline_button, start_send_cards_inline_button]
    picture_kb_builder.row(*buttons, width=1)
    return picture_kb_builder.as_markup()
