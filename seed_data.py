from backend import create_user, create_table, create_booking, get_all_bookings

print("--- Добавляем пользователей ---")
create_user('Иван', 'ivan@mail.ru')
create_user('Мария', 'maria@mail.ru')
create_user('Алексей', 'alex@mail.ru')

print("--- Добавляем столики ---")
create_table(1, 4)
create_table(2, 2)
create_table(3, 6)

print("--- Добавляем бронирования ---")
create_booking(1, 1, '2026-11-24 18:00', '2026-11-24 20:00')
create_booking(2, 2, '2026-11-24 19:00', '2026-11-24 21:00')

print("--- Проверяем, что всё записалось ---")
get_all_bookings()