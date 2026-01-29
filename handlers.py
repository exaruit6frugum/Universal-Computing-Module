import sys
from menus import *
from computing_core import *

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def execute_exit():
    """Функция завершения программы"""
    print(f"\n{BLUE}Завершение программы...{RESET}")
    sys.exit()


def handle_elementary_menu(user_option):
    """Обработчик ответа пользователя в меню элементарных операций"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            process_user_input(sum_nums, 2)
            return "elementary_menu"
        elif user_option == 2:
            return "elementary_menu"
        elif user_option == 3:
            return "elementary_menu"
        elif user_option == 4:
            return "elementary_menu"
        elif user_option == 5:
            return "elementary_menu"
        elif user_option == 6:
            return "elementary_menu"
        elif user_option == 7:
            return "elementary_menu"
        elif user_option == 8:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 8.{RESET}")
        return "elementary_menu"


def handle_finance_menu(user_option):
    """Обработчик ответа пользователя в меню элементарных операций"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            return "finance_menu"
        elif user_option == 2:
            return "finance_menu"
        elif user_option == 3:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 3.{RESET}")
        return "finance_menu"


def handle_statistics_menu(user_option):
    """Обработчик ответа пользователя в меню элементарных операций"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            return "statistics_menu"
        elif user_option == 2:
            return "statistics_menu"
        elif user_option == 3:
            return "statistics_menu"
        elif user_option == 4:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 4.{RESET}")
        return "statistics_menu"

def handle_trigonometry_menu(user_option):
    """Обработчик ответа пользователя в меню элементарных операций"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            return "trigonometry_menu"
        elif user_option == 2:
            return "trigonometry_menu"
        elif user_option == 3:
            return "trigonometry_menu"
        elif user_option == 4:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 4.{RESET}")
        return "trigonometry_menu"


def handle_num_theory_menu(user_option):
    """Обработчик ответа пользователя в меню элементарных операций"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            return "num_theory_menu"
        elif user_option == 2:
            return "num_theory_menu"
        elif user_option == 3:
            return "num_theory_menu"
        elif user_option == 4:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 4.{RESET}")
        return "num_theory_menu"

def handle_num_systems_menu(user_option):
    """Обработчик ответа пользователя в меню элементарных операций"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            return "num_systems_menu"
        elif user_option == 2:
            return "num_systems_menu"
        elif user_option == 3:
            return "num_systems_menu"
        elif user_option == 4:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 4.{RESET}")
        return "num_systems_menu"


def handle_main(user_option):
    """Обработчик ответа пользователя в главном меню"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            return "elementary_menu"
        elif user_option == 2:
            return "finance_menu"
        elif user_option == 3:
            return "statistics_menu"
        elif user_option == 4:
            return "trigonometry_menu"
        elif user_option == 5:
            return "num_theory_menu"
        elif user_option == 6:
            return "num_systems_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 6.{RESET}")
        return "main_menu"