"""
Домашнее задание №1
Функции и структуры данных
"""

import math

def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(el ** 2 for el in args)

print(power_numbers(1, 2, 5, 7))




# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    # список простых чисел начинается с 2, всё остальное можно сразу отмести
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    # Если число не простое, то в отрезке от 1 до квадратного корня числа, точно будут его делители.
    for element in divisors:
        if number % element == 0:
            return False
    return True

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False


def filter_numbers(numbers, mode='prime'):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    lst=[]
    if mode.upper() == 'PRIME':
        for i in numbers:
            if is_prime(i):
                lst.append(i)
    if mode.upper() == 'ODD':
        for i in numbers:
            if is_odd(i):
                lst.append(i)
    if mode.upper() == 'EVEN':
        for i in numbers:
            if is_even(i):
                lst.append(i)
    return lst

print(filter_numbers(list(range(1, 20)), 'prime'))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 'odd'))
print(filter_numbers(list(range(1, 30)), 'even'))
print(filter_numbers(list(range(1, 30))))


