from backend import get_all_bookings, check_table_availability, create_booking

def main():
    print("🍽️  Добро пожаловать в систему бронирования!")
    
    while True:
        print("\nВыберите действие:")
        print("1. Показать все бронирования")
        print("2. Проверить доступность стола")
        print("3. Выход")
        
        choice = input("Введите номер (1-3): ").strip()
        
        if choice == '1':
            get_all_bookings()
            
        elif choice == '2':
            try:
                table_id = int(input("Введите ID стола (1, 2 или 3): "))
                date = input("Введите дату (ГГГГ-ММ-ДД, например 2026-11-25): ")
                start = input("Введите время начала (ЧЧ:ММ, например 18:00): ")
                end = input("Введите время конца (ЧЧ:ММ, например 20:00): ")
                
                check_table_availability(table_id, date, start, end)
            except ValueError:
                print("❌ Неверный формат данных!")
                
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("❌ Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
