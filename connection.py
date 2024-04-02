from dotenv import load_dotenv
import os


# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение адреса БД из переменных окружения
DATABASE_URL = os.getenv('DATABASE_URL')
