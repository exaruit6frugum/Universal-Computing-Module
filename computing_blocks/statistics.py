RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def run_calculation_statistics(func, type_of_operation):
    """Функция ввода данных от пользователя и их обработки вычислительной функцией"""
    nums = []
    try:
        print("\n" + "-" * 100)
        print(f"Операция: {BLUE}{type_of_operation}{RESET}")

        num_of_numbers = int(input("Введите количество чисел: "))
        word_form = "числа"
        if num_of_numbers == 1:
            word_form = "число"
        if num_of_numbers > 4:
            word_form = "чисел"

        print(f"Введите {num_of_numbers} {word_form}:")

        i = 0
        while i < num_of_numbers:
            user_input = input(f"Число №{i + 1}: ")
            nums.append(float(user_input))
            i += 1

    except ValueError:
        print(f"{RED}Некорректный ввод: Введите число.{RESET}")

    try:
        result = func(nums)
        print(f"\n{GREEN}Операция успешно выполнена!{RESET}\n{BLUE}Результат: {result}{RESET}")
    except Exception as error:
        print(f"\n{RED}{error}{RESET}")

    print("-" * 100)

def average_mean(nums):
    sum = 0
    for num in nums:
        sum += num
    average = sum / len(nums)
    return average