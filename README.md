# Система бронирования столов (booking_system)

## Установка и запуск

1. Создайте виртуальное окружение:
   python3 -m venv venv
   source venv/bin/activate

2. Установите зависимости:
   pip install -r requirements.txt

3. Создайте файл .env на основе .env.example:
   cp .env.example .env

4. Создайте базу данных booking_db в pgAdmin и выполните SQL для создания таблиц users, tables, bookings.

5. Запустите тестовые данные:
   python3 test_data.py

6. Запустите CLI-приложение:
   python3 app.py

## Структура проекта

- postgres_driver.py — подключение к БД через psycopg2 + dotenv
- backend.py — CRUD-функции и проверка доступности
- app.py — CLI-меню
- test_data.py — тестовое заполнение БД

## Что реализовано

- Подключение к PostgreSQL через .env
- CRUD для моделей User, Table, Booking
- Функция check_table_availability с запретом пересекающихся бронирований
- CLI-меню с проверкой доступности
- ON DELETE CASCADE для связанных записей
