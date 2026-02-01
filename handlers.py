from computing_blocks.statistics import *
from computing_blocks.elementary import *
from menus import *
import sys

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
            run_calculation_elementary(sum_nums, 2, "Сложение")
        elif user_option == 2:
            run_calculation_elementary(difference_nums, 2, "Вычитание")
        elif user_option == 3:
            run_calculation_elementary(prod_nums, 2, "Умножение")
        elif user_option == 4:
            run_calculation_elementary(divide_nums, 2, "Деление")
        elif user_option == 5:
            run_calculation_elementary(exponentiation_num, 2, "Возведение в степень")
        elif user_option == 6:
            run_calculation_elementary(sqrt_num, 1, "Извлечение квадратного корня")
        elif user_option == 7:
            run_calculation_elementary(cube_root_num, 1, "Извлечение кубического корня")
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
            return "finance_menu"
        elif user_option == 4:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 4.{RESET}")
        return "finance_menu"


def handle_statistics_menu(user_option):
    """Обработчик ответа пользователя в меню элементарных операций"""
    try:
        user_option = int(user_option)
        if user_option == 0:
            return execute_exit()
        elif user_option == 1:
            run_calculation_statistics(average_mean, "Среднее арифметическое")
            return "statistics_menu"
        elif user_option == 2:
            return "statistics_menu"
        elif user_option == 3:
            return "statistics_menu"
        elif user_option == 4:
            return "statistics_menu"
        elif user_option == 5:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 5.{RESET}")
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
            return "trigonometry_menu"
        elif user_option == 5:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 5.{RESET}")
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
            return "num_theory_menu"
        elif user_option == 5:
            return "num_theory_menu"
        elif user_option == 6:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только цифру от 0 до 6.{RESET}")
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
            return "num_systems_menu"
        elif user_option == 5:
            return "main_menu"
        else:
            raise ValueError
    except ValueError:
        print(f"\n{RED}Некорректный ввод: Введите только две цифры от 1 до 4 или одну цифру для завершения программы/возвращения к главному меню.{RESET}")
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