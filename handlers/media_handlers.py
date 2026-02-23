from aiogram import Router, types, F
from aiogram.filters.command import Command

router = Router()

@router.message(F.photo)
async def handle_photo(message: types.Message):
    await message.answer('Не присылай мне фотки клоун')

@router.message(F.sticker)
async def handle_sticker(message: types.Message):
    await message.answer('Мог бы и ещё хуже стикер поискать')

@router.message(F.audio)
async def handle_audio(message: types.Message):
    await message.answer("ХУЕТА ТВОЙ ТРЕК УДАЛИ БЫСТРО!")

