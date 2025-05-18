# 1
print("############################")
####
numbers = [1, 4, 6, 7, 9, 2, 3, 10, 5, 8]
result = list(filter(lambda x: x < 5, numbers))
print(result)  # [1, 4, 2, 3]
####
numbers = [10, 20, 30, 40, 50]
result = list(map(lambda x: x / 2, numbers))
print(result)  # [5.0, 10.0, 15.0, 20.0, 25.0]
####
numbers = [15, 18, 20, 22, 17, 25, 30]
filtered = filter(lambda x: x > 17, numbers)
result = list(map(lambda x: x / 2, filtered))
print(result)  # [9.0, 10.0, 11.0, 12.5, 15.0]
####
numbers = range(10, 100)
filtered = filter(lambda x: x % 9 == 0, numbers)
squared = map(lambda x: x ** 2, filtered)
result = sum(squared)
print(result)
####

print("############################")
# 2
def factorials(n1):
    current_factorial = 1
    for i in range(1, n1 + 1):
        current_factorial *= i
        yield current_factorial

n = 7
for fact in factorials(n):
    print(fact, end=' ')
print ("")
print("############################")
# 3
def square_fibonacci(n1):
    a, b = 0, 1
    for _ in range(n1):
        yield b ** 2
        a, b = b, a + b
n = 7
print(*square_fibonacci(n))
print("############################")
# 4
def russian_alphabet():
    # Коды букв 'а' до 'я' в Unicode (1072 до 1103)
    for code in range(1072, 1104):
        yield chr(code)

for letter in russian_alphabet():
    print(letter, end=' ')

print("")
print("############################")
# 5
alphabet = (chr(code) for code in range(1072, 1104))  # 'а' = 1072, 'я' = 1103

# Пример использования:
print(*alphabet)
print("############################")
# 6
def arithmetic_operation(operation1):
    if operation1 == '+':
        return lambda x, y: x + y
    elif operation1 == '-':
        return lambda x, y: x - y
    elif operation1 == '*':
        return lambda x, y: x * y
    elif operation1 == '/':
        return lambda x, y: x / y
    else:
        raise ValueError("Неподдерживаемая операция")

operation = arithmetic_operation('+')
print(operation(1, 4))

operation = arithmetic_operation('-')
print(operation(6, 2))

operation = arithmetic_operation('*')
print(operation(1, 9))

operation = arithmetic_operation('/')
print(operation(21, 3))
print("############################")
#7
def same_by(characteristic, objects):
    if not objects:  # Если список пустой, возвращаем True
        return True
    # Получаем характеристику первого элемента
    first_char = characteristic(objects[0])
    # Проверяем, что все остальные элементы имеют такую же характеристику
    return all(characteristic(x) == first_char for x in objects)

# Пример 1
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

# Пример 2
values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

print("############################")
#8
def print_operation_table(operation1, num_rows=9, num_columns=9):
    # Печатаем заголовок таблицы
    print(' '.join(f"{i:4}" for i in range(1, num_columns + 1)))

    # Печатаем строки таблицы
    for row in range(1, num_rows + 1):
        # Печатаем номер строки
        print(f"{row:<4}", end='')
        # Печатаем значения ячеек
        for col in range(1, num_columns + 1):
            print(f"{operation1(row, col):4}", end='')
        print()  # Переход на новую строку


print_operation_table(lambda x, y: x * y)
print("############################")
#9
def ask_password(login, password, success, failure):
    login_lower = login.lower()
    password_lower = password.lower()

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    # Проверка количества гласных
    password_vowels = [c for c in password_lower if c in vowels]
    vowel_count_ok = len(password_vowels) == 3

    # Получаем согласные из логина и пароля
    login_consonants = [c for c in login_lower if c not in vowels]
    password_consonants = [c for c in password_lower if c not in vowels]

    consonants_ok = login_consonants == password_consonants

    # Определяем тип ошибки
    if vowel_count_ok and consonants_ok:
        success(login)
    else:
        if not vowel_count_ok and not consonants_ok:
            failure(login, "Everything is wrong")
        elif not vowel_count_ok:
            failure(login, "Wrong number of vowels")
        else:
            failure(login, "Wrong consonants")


def main(login, password):
    def success(login):
        print(f"Привет, {login}!")

    def failure(login, error):
        print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {error.upper()}.")

    ask_password(login, password, success, failure)


main("login", "aaalgn")
main("login", "luagon")
main("login",
     "aaalg")
main("login",
     "aaalgnn")
main("login",
     "aaa")
print("############################")
#10
words = input().split()
sorted_words = sorted(words, key=lambda x: x.lower())
print(' '.join(sorted_words))
print("############################")
#11
numbers = list(map(int, input().split()))  # Ввод чисел через пробел
sorted_numbers = sorted(numbers, key=lambda x: abs(x), reverse=True)
print(' '.join(map(str, sorted_numbers)))
print("############################")
#12
def distance_squared(point):
    return point[0]**2 + point[1]**2

points = [tuple(map(int, point.split())) for point in input().split(', ')]
points.sort(key=lambda p: (distance_squared(p), p[0], p[1]))

print(*[f"({x}, {y})" for x, y in points])
print("############################")
#13
print(any(0 in row for row in [list(map(int, input().split())) for _ in range(int(input()))]))
print("############################")
#14
import sys
from collections import defaultdict

word_indices = defaultdict(int)
words = []

for line in sys.stdin:
    for word in line.split():
        if word[0].isupper():
            if word not in word_indices:
                word_indices[word] = len(word_indices)
            words.append(word)

for word in sorted(set(words)):
    print(f"{word_indices[word]} - {word}")

print("############################")
#15
import sys
from functools import reduce

result = reduce(
    lambda x, y: x if x < y else y,
    (line.strip() for line in sys.stdin)
)
print(result)
#16
print("############################")

import sys
from functools import reduce
from math import gcd

numbers = list(map(int, sys.stdin.read().split()))
result = reduce(gcd, numbers)
print(result)
#17
print("############################")
def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password != "secret":  # Здесь можно использовать любой проверочный пароль
            print("В доступе отказано")
            return None
        return func(*args, **kwargs)
    return wrapper

@check_password
def secret_function():
    print("Доступ к секретной функции получен!")

secret_function()
#18
print("############################")
def check_password(correct_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            password = input("Введите пароль: ")
            if password != correct_password:
                print("В доступе отказано")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator


@check_password('burger123')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print(f"Готовим бургер с мясом {typeOfMeat}")
    if withOnion:
        print("Добавляем лук")
    if withTomato:
        print("Добавляем помидор")
    return "Ваш бургер готов!"

# Тестирование
result = make_burger("говядина")
if result:
    print(result)
    print("############################")
#19
def cached(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper



@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Тестирование
print(fib(10))
print(fib(20))
print("############################")