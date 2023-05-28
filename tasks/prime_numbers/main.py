import sys


def find_prime_numbers(n):
    if not isinstance(n, int) or n <= 2:
        raise ValueError("N должно быть целым числом больше 2")

    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python3 main.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Некорректный ввод. N должно быть целым числом.")
        sys.exit(1)

    try:
        prime_numbers = find_prime_numbers(n)
        print(f"Простые числа до {n}:")
        print(prime_numbers)
    except ValueError as e:
        print(str(e))
        sys.exit(1)