from postgres_driver import init_db
from backend import (get_all_bookings, check_table_availability, 
                     create_user, get_all_users, 
                     create_table, get_all_tables)

def main():
    print("=== Запуск автосоздания таблиц ===")
    init_db()
    
    print("\n🍽️ Добро пожаловать в систему бронирования!")
    
    while True:
        print("\nГлавное меню:")
        print("1. Бронирования (список)")
        print("2. Проверить доступность стола")
        print("3. Пользователи (список и добавление)")
        print("4. Столы (список и добавление)")
        print("5. Выход")
        
        choice = input("Введите номер (1-5): ").strip()
        
        if choice == '1':
            get_all_bookings()
            
        elif choice == '2':
            try:
                table_id = int(input("Введите ID стола (1, 2 или 3): "))
                date = input("Введите дату (ГГГГ-ММ-ДД): ")
                start = input("Время начала (ЧЧ:ММ): ")
                end = input("Время конца (ЧЧ:ММ): ")
                check_table_availability(table_id, date, start, end)
            except ValueError:
                print("❌ Неверный формат данных!")
                
        elif choice == '3':
            print("\n1. Показать всех пользователей")
            print("2. Добавить пользователя")
            sub = input("Выбор (1-2): ").strip()
            if sub == '1':
                get_all_users()
            elif sub == '2':
                name = input("Имя: ")
                phone = input("Телефон: ")
                create_user(name, phone)
                
        elif choice == '4':
            print("\n1. Показать все столы")
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
