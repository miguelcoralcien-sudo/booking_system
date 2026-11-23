import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        return conn
    except Error as e:
        print(f"Ошибка подключения к БД: {e}")
        return None

def init_db():
    """Автосоздание таблиц при первом запуске."""
    conn = get_db_connection()
    if conn:
        try:
            with conn, conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS tables (
                        id SERIAL PRIMARY KEY,
                        table_number INT UNIQUE NOT NULL,
                        capacity INT NOT NULL CHECK (capacity > 0)
                    );
                    CREATE TABLE IF NOT EXISTS bookings (
                        id SERIAL PRIMARY KEY,
                        user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                        table_id INT NOT NULL REFERENCES tables(id) ON DELETE CASCADE,
                        booking_date DATE NOT NULL,
                        start_time TIME NOT NULL,
                        end_time TIME NOT NULL
                    );
                """)
                conn.commit()
                print("✅ Таблицы users, tables, bookings созданы (или уже существуют).")
        except Error as e:
            print(f"Ошибка создания таблиц: {e}")
        finally:
            conn.close()
