from postgres_driver import init_db
from backend import (get_all_bookings, check_table_availability, create_booking,
                     update_booking, delete_booking,
                     create_user, get_all_users,
                     create_table, get_all_tables)

def main():
    print("=== Запуск автосоздания таблиц ===")
    init_db()
    print("\n🍽️ Добро пожаловать в систему бронирования!")
    
    while True:
        print("\nГлавное меню:")
        print("1. Бронирования")
        print("2. Проверить доступность стола")
        print("3. Пользователи")
        print("4. Столы")
        print("5. Выход")
        
        choice = input("Введите номер (1-5): ").strip()
        
        if choice == '1':
            print("\nМеню бронирований:")
            print("1. Показать все")
            print("2. Создать бронирование")
            print("3. Обновить бронирование")
            print("4. Удалить бронирование")
            sub = input("Выбор (1-4): ").strip()
            if sub == '1':
                get_all_bookings()
            elif sub == '2':
                try:
                    uid = int(input("ID пользователя: "))
                    tid = int(input("ID стола: "))
                    date = input("Дата (ГГГГ-ММ-ДД): ")
                    start = input("Начало (ЧЧ:ММ): ")
                    end = input("Конец (ЧЧ:ММ): ")
                    create_booking(uid, tid, date, start, end)
                except ValueError:
                    print("❌ Неверный формат!")
            elif sub == '3':
                try:
                    bid = int(input("ID бронирования для обновления: "))
                    print("Оставьте поле пустым (просто нажмите Enter), если не меняете:")
                    uid = input("Новый ID пользователя: ").strip()
                    tid = input("Новый ID стола: ").strip()
                    date = input("Новая дата: ").strip()
                    start = input("Новое начало: ").strip()
                    end = input("Новый конец: ").strip()
                    update_booking(bid, 
                                   user_id=int(uid) if uid else None,
                                   table_id=int(tid) if tid else None,
                                   booking_date=date if date else None,
                                   start_time=start if start else None,
                                   end_time=end if end else None)
                except ValueError:
                    print("❌ Неверный формат!")
            elif sub == '4':
                try:
                    bid = int(input("ID бронирования для удаления: "))
                    delete_booking(bid)
                except ValueError:
                    print("❌ Неверный формат!")
                    
        elif choice == '2':
            try:
                table_id = int(input("Введите ID стола: "))
                date = input("Введите дату (ГГГГ-ММ-ДД): ")
                start = input("Время начала (ЧЧ:ММ): ")
                end = input("Время конца (ЧЧ:ММ): ")
                check_table_availability(table_id, date, start, end)
            except ValueError:
                print("❌ Неверный формат данных!")
                
        elif choice == '3':
            print("\nМеню пользователей:")
            print("1. Показать всех")
            print("2. Добавить пользователя")
            sub = input("Выбор (1-2): ").strip()
            if sub == '1':
                get_all_users()
            elif sub == '2':
                name = input("Имя: ")
                phone = input("Телефон: ")
                create_user(name, phone)
                
        elif choice == '4':
            print("\nМеню столов:")
            print("1. Показать все")
            print("2. Добавить стол")
            sub = input("Выбор (1-2): ").strip()
            if sub == '1':
                get_all_tables()
            elif sub == '2':
                try:
                    num = int(input("Номер стола: "))
                    cap = int(input("Количество мест: "))
                    create_table(num, cap)
                except ValueError:
                    print("❌ Неверный формат!")
                    
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("❌ Неверный выбор.")

if __name__ == "__main__":
    main()
