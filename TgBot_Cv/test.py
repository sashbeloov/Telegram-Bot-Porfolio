from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia
import asyncio

TOKEN = "7758945683:AAHMdKXctl6yDr1S6-4DM2zByqyBc6nTkbU"

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {}


@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start":
        await start(message)
    elif "language" not in user_data[user_id]:
        await bosh_menu(message)
    elif message.text == "Bog'lanish 📞":
        await contact(message)
    elif message.text == "CV Yuklash 📥":
        await cv_download_menu(message)
    elif message.text == "⬅️Ortga":
        await bosh_menu(message)


@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
         types.KeyboardButton(text="🇺🇸 English")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Assalomu Alaykum! Ushbu bot yordamida siz Chayka Aleksandrning portfoliosi bilan tanishib chiqasiz.😊\n\n"
        "Здравствуйте! С помощью этого бота вы сможете ознакомиться с портфолио Чайка Александра.😊\n\n"
        "Hello! With this bot, you can explore Chayka Aleksandr's portfolio.😊",
        reply_markup=keyboard)
    print(1, user_data)


async def bosh_menu(message: types.Message):
    user_id = message.from_user.id
    language = message.text
    user_data[user_id]["language"] = "language"
    button = [
        [types.KeyboardButton(text="Loyihalar 💻"), types.KeyboardButton(text="Tajriba 🧑‍💻")],
        [types.KeyboardButton(text="CV Yuklash 📥"), types.KeyboardButton(text="Bog'lanish 📞")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Quyidagi tugmalardan birini tanlang:\n\n"
        "💻 Loyihalar — Mening loyihalarim bilan tanishing.\n\n"
        "🧑‍💻 Tajriba — Tajribam haqida ma'lumot oling.\n\n"
        "📥 CV Yuklash — Rezyumeni yuklab olish.\n\n"
        "📞 Bog'lanish — Mening aloqalarimni ko‘rish.\n\n👇👇👇👇",
        reply_markup=keyboard
    )
    print(2, user_data)

# rasm joylash diskni o'zidan
async def cv_download_menu(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="⬅️Ortga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "images/CV-resume.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path,))
    await message.answer("Bu mening rezyumem. Yuklab oling! 😊", reply_markup=keyboard)
    print("CV yuborildi!")
    # C:\Users\Windows10\Desktop\TgBot_Cv\images


async def contact(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="Telegram ✉️"), types.KeyboardButton(text="Instagram 📸")],
        [types.KeyboardButton(text="Gmail 📧"), types.KeyboardButton(text="GitHub 💼")],
        [types.KeyboardButton(text="⬅️Ortga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Men bilan quyidagi platformalar orqali bog‘lanishingiz mumkin. Tugmalardan birini tanlang:\n👇👇👇👇",
        reply_markup=keyboard
    )


async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())
