from postgres_driver import get_db_connection

# === USER CRUD ===
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

def get_all_users():
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("SELECT id, name, phone FROM users ORDER BY id")
                users = cur.fetchall()
                print("\nСписок пользователей:")
                for u in users:
                    print(f"ID: {u[0]} | Имя: {u[1]} | Телефон: {u[2]}")
                return users
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

def update_user(user_id, name=None, phone=None):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                if name and phone:
                    cur.execute("UPDATE users SET name=%s, phone=%s WHERE id=%s", (name, phone, user_id))
                elif name:
                    cur.execute("UPDATE users SET name=%s WHERE id=%s", (name, user_id))
                elif phone:
                    cur.execute("UPDATE users SET phone=%s WHERE id=%s", (phone, user_id))
                conn.commit()
                print(f"Пользователь ID {user_id} обновлён.")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

def delete_user(user_id):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
                conn.commit()
                print(f"Пользователь ID {user_id} удалён (и его бронирования тоже — CASCADE).")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

# === TABLE CRUD ===
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

def get_all_tables():
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("SELECT id, table_number, capacity FROM tables ORDER BY id")
                tables = cur.fetchall()
                print("\nСписок столов:")
                for t in tables:
                    print(f"ID: {t[0]} | Номер: №{t[1]} | Мест: {t[2]}")
                return tables
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

def update_table(table_id, table_number=None, capacity=None):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                if table_number and capacity:
                    cur.execute("UPDATE tables SET table_number=%s, capacity=%s WHERE id=%s", (table_number, capacity, table_id))
                elif table_number:
                    cur.execute("UPDATE tables SET table_number=%s WHERE id=%s", (table_number, table_id))
                elif capacity:
                    cur.execute("UPDATE tables SET capacity=%s WHERE id=%s", (capacity, table_id))
                conn.commit()
                print(f"Стол ID {table_id} обновлён.")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

def delete_table(table_id):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("DELETE FROM tables WHERE id=%s", (table_id,))
                conn.commit()
                print(f"Стол ID {table_id} удалён (и его бронирования тоже — CASCADE).")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

# === BOOKING CRUD ===
def create_booking(user_id, table_id, booking_date, start_time, end_time):
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
                print(f"Бронирование создано с ID: {booking_id}")
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

def update_booking(booking_id, user_id=None, table_id=None, booking_date=None, start_time=None, end_time=None):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("SELECT user_id, table_id, booking_date, start_time, end_time FROM bookings WHERE id=%s", (booking_id,))
                row = cur.fetchone()
                if not row:
                    print("Бронирование не найдено.")
                    return
                uid, tid, bd, st, et = row
                uid = user_id or uid
                tid = table_id or tid
                bd = booking_date or bd
                st = start_time or st
                et = end_time or et
                cur.execute("UPDATE bookings SET user_id=%s, table_id=%s, booking_date=%s, start_time=%s, end_time=%s WHERE id=%s", (uid, tid, bd, st, et, booking_id))
                conn.commit()
                print(f"Бронирование ID {booking_id} обновлено.")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

def delete_booking(booking_id):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("DELETE FROM bookings WHERE id=%s", (booking_id,))
                conn.commit()
                print(f"Бронирование ID {booking_id} удалено.")
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            conn.close()

# === ПРОВЕРКА ДОСТУПНОСТИ ===
def check_table_availability(table_id, booking_date, start_time, end_time):
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("""
                    SELECT t.table_number FROM bookings b
                    JOIN tables t ON b.table_id = t.id
                    WHERE b.table_id = %s AND b.booking_date = %s
                    AND b.start_time < %s AND b.end_time > %s
                """, (table_id, booking_date, end_time, start_time))
                conflict = cur.fetchone()
                if conflict:
                    print(f"Стол №{conflict[0]} уже занят {booking_date} с {start_time} до {end_time}!")
                    return False
                else:
                    print(f"Стол №{table_id} свободен {booking_date} с {start_time} до {end_time}!")
                    return True
        except Exception as e:
            print(f"Ошибка проверки: {e}")
            return False
        finally:
            conn.close()
