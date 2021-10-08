import telebot
from datetime import date

token = '2078435521:AAHhcJXw_hrPwAYPD38wsukCZm16FWCBN2A'
CHANNEL_NAME = '@shue_pepesha'
wednesday = 2
bot = telebot.TeleBot(token)
bot.send_sticker(CHANNEL_NAME, "https://rabota-bot.github.io/webp.webp")
if date.today().weekday() != wednesday:
    bot.send_message(CHANNEL_NAME, date.today().weekday() - wednesday)
bot.send_sticker(CHANNEL_NAME, "https://rabota-bot.github.io/webp1.webp")


