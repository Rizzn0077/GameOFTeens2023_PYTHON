import os
import string
import random
import time
import requests
from pathlib import Path
from settings import *
from aiogram import *
from aiogram.types import *
from packages import *


bot = Bot(TOKEN)
dp = Dispatcher(bot)

package = KeyboardButton('📃Підібрати тарифи')
info = KeyboardButton('🤔Інформація про Lifecell')
commands = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(package).add(info)

price_r_opt1 = KeyboardButton('🪙До 160 грн.')
price_r_opt2 = KeyboardButton('💰До 325 грн.')
price_r_opt3 = KeyboardButton('👑Вище 325 грн.')
price_range = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(price_r_opt1).add(price_r_opt2).add(price_r_opt3)

internet_r_opt1 = KeyboardButton('📶До 500 МБ. на день.')
internet_r_opt2 = KeyboardButton('📶До 7 ГБ.')
internet_r_opt3 = KeyboardButton('📶До 8 ГБ.')
internet_range = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(internet_r_opt1).add(internet_r_opt2).add(internet_r_opt3)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, '''👋Привіт!

🤔Lifecell Assist - один із ботів, який був створений щоб допомогти тобі з Lifecell.

‼️Зараз у вас на єкрані потрібен бути інтерфейс команд. Будь ласка, виберіть одну з них.

⁉️Щоб подивитися усі слеш команди, введіть у чат \'/\'.''', reply_markup=commands)


@dp.message_handler()
async def all_reply_buttons_here(message: types.Message):
    chat_id = message.chat.id
    if message.text == '🤔Інформація про Lifecell':
        await message.answer('''Lifecell - українська телекомунікаційна компанія, третій за величиною оператор мобільного зв'язку в Україні.

Належить компанії Euroasia Telecommunications Holding BV (Нідерланди), якою в свою чергу володіє турецький оператор Turkcell. 

Надає послуги у стандартах GSM, UMTS, LTE та LTE Advanced.''', reply_markup=commands)
    if message.text == '📃Підібрати тарифи':
        await message.answer('‼️Поки що я вмію підбірати тарифи тільки за ціновими діапозонами, але у майбутньому є шанс що з\'являться й іншні види підбірки.')
        time.sleep(0.6)
        await bot.send_message(chat_id, '❓Який ціновий діапозон ви готові витратити на тариф?', reply_markup=price_range)
    if message.text == '🪙До 160 грн.':
        await message.answer('⌚Підбираємо тарифи, будь ласка зачекайте..')
        time.sleep(4)
        await bot.send_message(chat_id, '‼️Тарифи за вказаним діапозоном знайдені!')
        time.sleep(0.8)
        await bot.send_message(chat_id, price_opt1, reply_markup=commands)
    if message.text == '💰До 325 грн.':
        await message.answer('⌚Підбираємо тарифи, будь ласка зачекайте..')
        time.sleep(4)
        await bot.send_message(chat_id, '‼️Тарифи за вказаним діапозоном знайдені!')
        time.sleep(0.8)
        await bot.send_message(chat_id, price_opt1, disable_web_page_preview=True)
        await bot.send_message(chat_id, price_opt2, disable_web_page_preview=True, reply_markup=commands)
    if message.text == '👑Вище 325 грн.':
        await message.answer('⌚Підбираємо тарифи, будь ласка зачекайте..')
        time.sleep(4)
        await bot.send_message(chat_id, '‼️Тарифи за вказаним діапозоном знайдені!')
        time.sleep(0.8)
        await bot.send_message(chat_id, price_opt3, disable_web_page_preview=True, reply_markup=commands)


if __name__ == "__main__":
    executor.start_polling(dp)
