from asyncio import sleep
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram import Router, Bot, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, PollAnswer, CallbackQuery, \
    InputMediaPhoto, InputFile
from aiogram.fsm.state import default_state
from aiogram.types import FSInputFile


from tgbot.DB.filed_pictures import GetPictureFomFile
from tgbot.buisnes.buisnes_logic import GetKnowledgeFromPicture
from tgbot.buisnes.interface import GetConstitutionKnowledges
from tgbot.keyboards.inline_keyboards import  create_picture_inline_keyboard
from tgbot.lexicon.lixicon_ru import BotAnswers, LEXICON_RU

router = Router()
business_logic:GetConstitutionKnowledges = GetKnowledgeFromPicture(
    picture_repo=GetPictureFomFile(
        picture_dir=r'D:\python projects\non_comertial\constitution\pictures'))



@router.callback_query(Text(text=['start_send_cards_inline_button', 'get_one_more_card']))
async def process_start_giving_cards(callback: CallbackQuery, bot: Bot):
    keyboard = create_picture_inline_keyboard()
    await bot.send_chat_action(chat_id=callback.from_user.id, action='typing')
    await sleep(1)
    photo = FSInputFile(business_logic.send_knowledge())

    if not callback.message.photo:
        # Если фото нет, отправляем новое сообщение с фото
        await callback.message.answer_photo(photo=photo, reply_markup=keyboard)
    else:
        # Если фото есть, редактируем сообщение
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=photo,
            ),
            reply_markup=keyboard
        )