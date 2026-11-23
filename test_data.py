from postgres_driver import init_db
from backend import create_user, create_table, create_booking, get_all_bookings

print("=== Запуск автосоздания таблиц ===")
init_db()

print("\n=== Добавляем пользователей ===")
user1 = create_user("Алиса", "+79001111111")
user2 = create_user("Боб", "+79002222222")
user3 = create_user("Чарли", "+79003333333")

print("\n=== Добавляем столы ===")
table1 = create_table(1, 2)
table2 = create_table(2, 4)
table3 = create_table(3, 6)

print("\n=== Добавляем бронирования ===")
booking1 = create_booking(user1, table1, "2026-11-25", "18:00", "20:00")
booking2 = create_booking(user2, table2, "2026-11-25", "19:00", "21:00")

print("\n=== Проверяем все бронирования ===")
get_all_bookings()
