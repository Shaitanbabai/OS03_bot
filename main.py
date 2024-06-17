import telebot
from config import Config

bot = telebot.TeleBot(Config.TELEGRAM_API_TOKEN)
message_count = 0


# Обработчик всех входящих сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Этот бот лежит на локальном сервере с автозапуском')


# Запуск получения обновлений
bot.polling()
