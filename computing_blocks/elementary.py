import numpy as np

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def run_calculation(func, num_of_numbers, type_of_operation):
    """Функция ввода данных от пользователя и их обработки вычислительной функцией"""
    word_form = "числа"
    if num_of_numbers == 1:
        word_form = "число"
    if num_of_numbers > 4:
        word_form = "чисел"

    print("\n" + "-" * 100)
    print(f"Операция: {BLUE}{type_of_operation}{RESET}")
    print(f"Введите {num_of_numbers} {word_form}:")
    nums = []

    i = 0
    while i < num_of_numbers:
        try:
            user_input = input(f"Число №{i + 1}: ")
            nums.append(float(user_input))
            i += 1
        except ValueError:
            print(f"{RED}Некорректный ввод: Введите число.{RESET}")

    try:
        result = func(*nums)
        print(f"\n{GREEN}Операция успешно выполнена!{RESET}\n{BLUE}Результат: {result}{RESET}")

    except ZeroDivisionError:
        print(f"\n{RED}Ошибка: Деление на ноль.{RESET}")

    except ValueError as e:
        print(f"\n{RED}{e}{RESET}")

    print("-" * 100)


def sum_nums(first, second):
    return first + second

def difference_nums(first, second):
    return first - second

def prod_nums(first, second):
    return first * second

def divide_nums(first, second):
    return first / second

def exponentiation_num(num, power):
    return num ** power

def sqrt_num(num):
    if num < 0:
        raise ValueError("Ошибка: Квадратный корень из отрицательного числа.")
    return num ** 0.5

def cube_root_num(num):
    return num ** (1/3)