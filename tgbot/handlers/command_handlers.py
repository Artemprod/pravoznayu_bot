
from asyncio import sleep
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram import Router, Bot
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, PollAnswer
from aiogram.fsm.state import default_state

from tgbot.keyboards.inline_keyboards import create_start_inline_keyboard
from tgbot.lexicon.lixicon_ru import BotAnswers, LEXICON_RU

router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext, bot: Bot):
    keyboard = create_start_inline_keyboard()
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await message.answer(f'{BotAnswers.GREETINGS.value}',
                         reply_markup=keyboard)



# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands='help'), StateFilter(default_state))
async def process_help_command(message: Message, bot: Bot):
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await message.answer(f'{BotAnswers.HELP.value}',
                         )


@router.message(Command(commands='feedback'), ~StateFilter(default_state))  # фидбек ввиде web_app notion форма
async def process_feedback_command_state(message: Message, bot: Bot):
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)


@router.message(Command(commands='quiz'), ~StateFilter(default_state))
async def process_feedback_command_state(message: Message, bot: Bot):
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    # Сбрасываем состояние
    await message.answer(f'{BotAnswers.CANCEL.value + str(state.get_state())}', )
    await state.clear()
