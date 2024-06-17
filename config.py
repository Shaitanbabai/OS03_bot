from dotenv import load_dotenv
import os

#  Загрузка переменных окружения из .env файла
load_dotenv()


class Config:
    # Токен Telegram API
    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN', 'your-telegram-api-token-here')


# Пример использования:
if __name__ == "__main__":
    print("Telegram API Token:", Config.TELEGRAM_API_TOKEN)
