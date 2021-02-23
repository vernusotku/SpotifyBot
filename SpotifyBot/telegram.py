import telebot
import requests
import threading
from SpotifyBot import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет привет!")

@bot.message_handler(commands=['google'])
def google(message):
    bot.reply_to(message, requests.get("https://www.google.com").text[0:10])

th = threading.Thread(target=bot.polling)
th.start()