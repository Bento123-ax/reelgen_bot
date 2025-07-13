from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import random
import os

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ideas = [
    {
        "тема": "кофе",
        "эмоция": "юмор",
        "идея": "До/после кофе — ты как зомби, потом супергерой",
        "трек": "Yeat – Hottest",
        "текст": "«Поки не випив — не людина 😵☕»"
    },
    {
        "тема": "спорт",
        "эмоция": "мотивация",
        "идея": "Подъём в 5 утра, холод, тренировка, результат",
        "трек": "Eminem – Till I Collapse",
        "текст": "«Ніхто не зробить це за тебе»"
    }
]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Привіт! Я бот-генератор ідей для Reels/TikTok/Shorts\n\nНапиши мені тему ролика, наприклад: «кофе» або «спорт»")

@dp.message_handler()
async def generate_idea(message: types.Message):
    user_input = message.text.lower()
    result = next((i for i in ideas if i['тема'] in user_input), random.choice(ideas))
    response = (
        f"🎥 Ідея: {result['идея']}\n"
        f"🎭 Емоція: {result['эмоция']}\n"
        f"🎵 Трек: {result['трек']}\n"
        f"✍️ Текст: {result['текст']}"
    )
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
