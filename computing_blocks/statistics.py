from colors import *
import numpy as np

def run_calculation_statistics(func, type_of_operation):
    """Функция запуска вычислений категории 'Статистика' с пользовательским вводом.\n
    Запрашивает у пользователя числа, передаёт их в вычислительную функцию и выводит результат.\n
    Args: func, str."""

    nums = []
    print("\n\n" + "-" * 100)
    print(f"Операция: {BLUE}{type_of_operation}{RESET}")

    num_of_numbers = 0
    while num_of_numbers <= 0:
        try:
            num_of_numbers = int(input("▶ Введите количество чисел: "))
            if num_of_numbers <= 0 or not isinstance(num_of_numbers, int):
                raise ValueError
        except ValueError:
            print(f"{RED}⚠ Некорректный ввод: Введите положительное целое число.{RESET}")

    word_form = "числа"
    if num_of_numbers == 1:
        word_form = "число"
    if num_of_numbers > 4:
        word_form = "чисел"

    print(f"▶ Введите {num_of_numbers} {word_form}:\n")
    i = 0
    while i < num_of_numbers:
        try:
            user_input = input(f"Число №{i + 1}: ")
            nums.append(float(user_input))
            i += 1
        except ValueError:
            print(f"{RED}⚠ Некорректный ввод: Введите число.{RESET}")

    try:
        result = func(nums)
        print(f"\n{GREEN}✓ Операция успешно выполнена!{RESET}\n{BLUE}Результат: {result}{RESET}")
    except Exception as error:
        print(f"\n{RED}⚠ Ошибка: {error}{RESET}")

    print("-" * 100)


def average_mean(nums):
    nums = np.array(nums)
    average = np.sum(nums) / len(nums)
    return average

def median_and_mode(nums):
    nums.sort()
    length = len(nums)

    try:
        nums = [int(elem) for elem in nums]
    except ValueError:
        raise ValueError("Данная операция поддерживается только для целых чисел.")

    if length % 2 == 1:
        median = nums[length // 2]
    else:
        median = (nums[length // 2 - 1] + nums[length // 2]) / 2

    # Алгоритм нахождения моды (с учётом отрицательных чисел)
    mode = []
    if nums[0] < 0:
        min_nums = abs(min(nums))
    else:
        min_nums = 0
    repetitions = [0] * (min_nums + max(nums) + 1)

    for i in range(length):
        if nums[i] <= 0:
            repetitions[abs(nums[i])] += 1
        else:
            repetitions[nums[i] + min_nums] += 1
    max_repetition = max(repetitions)

    # Наиболее повторяющимся элементом в nums будет индекс наибольшего элемента в repetitions
    # Получаем этот индекс (первого попавшегося элемента из repetitions со значением max_repetition) и удаляем этот элемент,
    # так как мод может быть несколько

    index_shift = 0  # Переменная сдвига индексов, так как удаляем элемент из repetitions
    while max(repetitions) == max_repetition & max_repetition != 1:
        index = repetitions.index(max_repetition)
        if index > min_nums:
            add_num = index + index_shift - min_nums
        else:
            add_num = -(index + index_shift)
        mode.append(add_num)
        repetitions.pop(index)
        index_shift += 1

    mode.sort()
    result = f"\nМедиана: {median}\n"
    if len(mode) == 0:
        result += "Моды нет: Все элементы уникальные"
    elif len(mode) == 1:
        result += f"Мода: {mode[0]}"
    else:
        result += f"Несколько мод: "
        for i in range(len(mode)):
            result += f"{mode[i]}, "
        result = result[:-2]

    return result

def dispersion_and_deviation(nums):
    nums = np.array(nums)
    dispersion = average_mean(nums ** 2) - average_mean(nums) ** 2
    deviation = np.sqrt(dispersion)

    result = f"\nДисперсия: {dispersion:.4f}\nСтандартное отклонение: {deviation:.4f}"
    return result
