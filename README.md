# Система бронирования столов (booking_system)

## Установка и запуск

1. Создайте виртуальное окружение и активируйте его:
   python3 -m venv venv
   source venv/bin/activate

2. Установите зависимости:
   pip install -r requirements.txt

3. Создайте файл .env на основе .env.example:
   cp .env.example .env
   (Укажите в нем ваш пароль от PostgreSQL)

4. Создайте пустую базу данных `booking_db` в pgAdmin.
   Таблицы создадутся автоматически при первом запуске скрипта!

5. Запустите тестовые данные (создаст таблицы, пользователей, столы и брони):
   python3 test_data.py

6. Запустите CLI-приложение с полным меню:
   python3 app.py

## Структура проекта

- postgres_driver.py — подключение к БД и функция автосоздания таблиц (init_db)
- backend.py — полный CRUD для всех моделей и проверка доступности
- app.py — CLI-меню для управления пользователями, столами и бронированиями
- models/ — файлы моделей (user.py, table.py, booking.py)
- test_data.py — скрипт для тестового заполнения БД

## Что реализовано

- Подключение к PostgreSQL через .env
- Автосоздание таблиц при запуске (init_db)
- Полный CRUD (Create, Read, Update, Delete) для User, Table, Booking
- Функция check_table_availability с запретом пересекающихся бронирований
- Полное CLI-меню
- ON DELETE CASCADE для связанных записей
