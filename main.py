from menus import *
from handlers import *

def main():
    current_menu = "main_menu"
    next_menu = "main_menu"
    while True:
        if current_menu == "main_menu":
            show_main_menu()
            user_option = input(f"{GREEN}Ввод:{RESET} ")
            next_menu = handle_main(user_option)

        elif current_menu == "elementary_menu":
            show_elementary_menu()
            user_option = input(f"{GREEN}Выберите операцию:{RESET} ")
            next_menu = handle_elementary_menu(user_option)

        elif current_menu == "finance_menu":
            show_finance_menu()
            user_option = input(f"{GREEN}Выберите операцию:{RESET} ")
            next_menu = handle_finance_menu(user_option)

        elif current_menu == "statistics_menu":
            show_statistics_menu()
            user_option = input(f"{GREEN}Выберите операцию:{RESET} ")
            next_menu = handle_statistics_menu(user_option)

        elif current_menu == "trigonometry_menu":
            show_trigonometry_menu()
            user_option = input(f"{GREEN}Выберите операцию:{RESET} ")
            next_menu = handle_trigonometry_menu(user_option)

        elif current_menu == "num_theory_menu":
            show_num_theory_menu()
            user_option = input(f"{GREEN}Выберите операцию:{RESET} ")
            next_menu = handle_num_theory_menu(user_option)

        elif current_menu == "num_systems_menu":
            show_num_systems_menu()
            user_option = input(f"{GREEN}Выберите операцию:{RESET} ")
            next_menu = handle_num_systems_menu(user_option)

        else:
            print(f"\n{RED}Произошла ошибка: Обработчик ответа пользователя вернул некорректное значение.")
            print(f"Открываем главное меню...{RESET}")
            next_menu = "main_menu"

        current_menu = next_menu


if __name__ == "__main__":
    main()