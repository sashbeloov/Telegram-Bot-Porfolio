from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia, WebAppInfo
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
    elif message.text == "Ortga ↙️":
        await bosh_menu(message)
    elif message.text == "Telegram 📨":
        await tginfo(message)
    elif message.text == "⬅️ ️Ortga":
        await contact(message)
    elif message.text == "Instagram 📸":
        await instainfo(message)
    elif message.text == "GitHub 💼":
        await githubinfo(message)
    elif message.text == "️Ortga":
        await contact(message)
    elif message.text == "Loyihalar 💻":
        await loyihalar(message)
    elif message.text == "Portfolio 📍":
        await portfolio(message)
    elif message.text == "Mening-sitelarim 🌐":
        await mysites(message)
    elif message.text == "️Ortga ↘️":
        await loyihalar(message)







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
        [types.KeyboardButton(text="Ortga ↙️")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "../images/CV-resume.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path,))
    await message.answer("Bu mening rezyumem. Yuklab oling! 😊", reply_markup=keyboard)
    print("CV yuborildi!")
    # C:\Users\Windows10\Desktop\TgBot_Cv\images


async def contact(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="Telegram 📨"), types.KeyboardButton(text="Instagram 📸")],
        [types.KeyboardButton(text="Ortga ↙️")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Men bilan quyidagi platformalar orqali bog‘lanishingiz mumkin. Tugmalardan birini tanlang:\n👇👇👇👇",reply_markup=keyboard)




async def tginfo(message: types.Message):
    user_id = message.from_user.id
    button = [
        [types.KeyboardButton(text="⬅️ ️Ortga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Men bilan bog'lanish uchun kontaktlar: \n\nhttps://t.me/Belovsasha ✉️ \n\nTelefon raqam: +998-33-545-05-42 ☎️",reply_markup=keyboard)
    print('tg', user_data)




async def instainfo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["instainfo"] = "instainfo"
    buttons = [
        [types.InlineKeyboardButton(text="Instagramga havola",url="https://www.instagram.com/sashbeloov?igsh=MXNidW1nMGZ2ZWh2dw%3D%3D&utm_source=qr"),],
    ]
    file_path = "../images/instagram.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer("Instagram uchun havolani ustiga bosing: \n👇👇👇👇",reply_markup=keyboard)


async def loyihalar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["loyihalar"] = "loyihalar"
    button = [
        [types.KeyboardButton(text="Portfolio 📍")],
        [types.KeyboardButton(text="Mening-sitelarim 🌐"),types.KeyboardButton(text="GitHub 💼")],
        [types.KeyboardButton(text="Ortga ↙️")],
    ]
    file_path = "../images/myprojects.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Bu yerda siz menig Loyihalarim bilan tanishib chiqasiz 🧑‍💻\n",reply_markup=keyboard)


async def githubinfo(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["githubinfo"] = "githubinfo"
    button = [
        [types.InlineKeyboardButton(text="GitHubga havola",
                                    url="https://github.com/sashbeloov?tab=repositories")]
    ]
    file_path = "../images/GitHub-logo.png"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("GitHub orqali siz mening loyihalarimning kodlari bilan tanishib chiqishingiz mumkin 🗂\n\nGitHub uchun havolani ustiga bosing: \n👇👇👇👇",reply_markup=keyboard)



async def portfolio(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["portfolio"] = "portfolio"
    button = [
        [types.InlineKeyboardButton(text='Websiteni ochish',url="https://t.me/Aleksandr_Portfolioo_bot/Portfolio")]
    ]
    file_path = "../images/website.png"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("Bu tugmani bosish orqali siz mening portfolio websiteimga kirasiz 👇👇👇👇",reply_markup=keyboard)


async def mysites(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["mysites"] = "mysites"
    button = [
        [types.InlineKeyboardButton(text='Youtube klone', url="https://youtube-cloneuz.netlify.app/"),
         types.InlineKeyboardButton(text='Traveluz', url="https://sayohat-uz.netlify.app/")],
        [types.InlineKeyboardButton(text='Shoesuz', url="https://shoes-uz.netlify.app/"),
         types.InlineKeyboardButton(text='Fast-Food-Uz', url="https://fast-food-uz.netlify.app/")],
        [types.InlineKeyboardButton(text='Parralax-website', url="https://parralax-websitee.netlify.app/"),
         types.InlineKeyboardButton(text='Soat-uz', url="https://soat-uzz.netlify.app/")],
    ]
    file_path = "../images/websitee.jpg"
    await message.reply_photo(photo=types.FSInputFile(path=file_path, ))
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("Mening sitelarimni ko'rish uchun pastda turgan tugmalarni bosing \n👇👇👇👇👇👇",reply_markup=keyboard)






async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())




