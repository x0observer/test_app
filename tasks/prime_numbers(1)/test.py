from .main import find_prime_numbers

expected_output = [2, 3, 5, 7, 11, 13, 17, 19]
assert find_prime_numbers(20) == expected_output

# Проверка нахождения простых чисел до 30
expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert find_prime_numbers(30) == expected_output

# Проверка нахождения простых чисел до 50
expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
assert find_prime_numbers(50) == expected_output

# Проверка нахождения простых чисел до 100
expected_output = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97
]
assert find_prime_numbers(100) == expected_output

# Проверка с некорректным вводом
try:
    find_prime_numbers(1)
except ValueError as e:
    assert str(e) == "N должно быть целым числом больше 2"