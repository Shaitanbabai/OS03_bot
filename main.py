import telebot

# Указываем токен вашего бота
TOKEN = '7253573914:AAHXVvV9Du04ujMJ7SIwfPZePA1xr4YCS6s'

# Инициализация бота
bot = telebot.TeleBot(TOKEN)


# Обработчик всех входящих сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Этот бот лежит на локальном сервере с автозапуском')


# Запуск получения обновлений
bot.polling()
