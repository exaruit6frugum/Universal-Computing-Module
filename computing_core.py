import numpy as np

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def process_user_input(func, num_of_numbers):
    word_form = "числа"
    if num_of_numbers == 1:
        word_form = "число"
    if num_of_numbers > 4:
        word_form = "чисел"

    print(f"Введите {num_of_numbers} {word_form}:")
    nums = []

    for i in range(0, num_of_numbers):
        try:
            user_input = input(f"Число №{i + 1}: ")
            nums.append(int(user_input))
        except ValueError:
            i -= 1
            print(f"\n{RED}Некорректный ввод: Введите число.{RESET}\n")

    result = func(*nums)
    print(f"\n{GREEN}Операция успешно выполнена! Результат: {result}{RESET}\n")


def sum_nums(first, second):
    return first + second

def difference_nums(first, second):
    return first - second

def prod_nums(first, second):
    return first * second

def divide_nums(first, second):
    return first / second

def sqr_num(num):
    return num * num

def sqrt_num(num):
    return num ** 0,5

def cube_root_num(num):
    return num * 0.333333