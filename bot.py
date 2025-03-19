import telebot
from constants import BOT_KEY
from api import news

bot = telebot.TeleBot(BOT_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    text = 'Привет, я бот который по категории находит новости для тебя! Напиши категорию:'
    bot.send_message(chat_id=message.chat.id, text=text)

@bot.message_handler(content_types=['text'])
def find_news(message):
    text = news.get_news_with_category(message.text)
    bot.send_message(chat_id=message.chat.id, text=text)

if __name__ == "__main__":
    bot.polling(non_stop=True, interval=1)
