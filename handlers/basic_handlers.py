from aiogram import Router, types, F
from aiogram.filters.command import Command

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('ЫЫЫЫ ЫЫЫЫ Я повторяю за тобой ЫЫЫЫ ЫЫЫЫ')

@router.message(F.text)
async def handle_text(message: types.Message):
    await message.answer(f'ЫЫЫ ЫЫЫ ты написал - {message.text}')