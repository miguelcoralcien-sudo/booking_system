from postgres_driver import get_db_connection

def create_user(name, phone):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("INSERT INTO users (name, phone) VALUES (%s, %s) RETURNING id", (name, phone))
                user_id = cur.fetchone()[0]
                print(f"Пользователь '{name}' создан с ID: {user_id}")
                return user_id
        except Exception as e:
            print(f"Ошибка создания пользователя: {e}")
        finally:
            conn.close()

def create_table(table_number, capacity):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("INSERT INTO tables (table_number, capacity) VALUES (%s, %s) RETURNING id", (table_number, capacity))
                table_id = cur.fetchone()[0]
                print(f"Стол №{table_number} (на {capacity} мест) создан с ID: {table_id}")
                return table_id
        except Exception as e:
            print(f"Ошибка создания стола: {e}")
        finally:
            conn.close()

def check_table_availability(table_id, booking_date, start_time, end_time):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                # Проверяем пересечение времени: новое начало < существующего конца И новое конец > существующего начала
                cur.execute("""
                    SELECT t.table_number FROM bookings b
                    JOIN tables t ON b.table_id = t.id
                    WHERE b.table_id = %s AND b.booking_date = %s
                    AND b.start_time < %s AND b.end_time > %s
                """, (table_id, booking_date, end_time, start_time))
                
                conflict = cur.fetchone()
                if conflict:
                    print(f"❌ Стол №{conflict[0]} уже занят {booking_date} с {start_time} до {end_time}!")
                    return False
                else:
                    print(f"✅ Стол №{table_id} свободен {booking_date} с {start_time} до {end_time}!")
                    return True
        except Exception as e:
            print(f"Ошибка проверки: {e}")
            return False
        finally:
            conn.close()

def create_booking(user_id, table_id, booking_date, start_time, end_time):
    # Сначала проверяем доступность!
    if not check_table_availability(table_id, booking_date, start_time, end_time):
        return None
        
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO bookings (user_id, table_id, booking_date, start_time, end_time) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                    (user_id, table_id, booking_date, start_time, end_time)
                )
                booking_id = cur.fetchone()[0]
                print(f"✅ Бронирование создано с ID: {booking_id}")
                return booking_id
        except Exception as e:
            print(f"Ошибка создания бронирования: {e}")
        finally:
            conn.close()

def get_all_bookings():
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("""
                    SELECT b.id, u.name, t.table_number, b.booking_date, b.start_time, b.end_time
                    FROM bookings b
                    JOIN users u ON b.user_id = u.id
                    JOIN tables t ON b.table_id = t.id
                    ORDER BY b.booking_date, b.start_time
                """)
                bookings = cur.fetchall()
                print("\nСписок всех бронирований:")
                if not bookings:
                    print("Бронирований пока нет.")
                for b in bookings:
                    print(f"ID: {b[0]} | Клиент: {b[1]} | Стол: №{b[2]} | Дата: {b[3]} | Время: {b[4]} - {b[5]}")
                print("\n")
                return bookings
        except Exception as e:
            print(f"Ошибка получения бронирований: {e}")
        finally:
            conn.close()
