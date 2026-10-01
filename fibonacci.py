def fibonacci(n: int) -> int:
    """Обчислення n-го числа Фібоначчі ітеративно."""
    if n < 0:
        raise ValueError("Число n має бути невід'ємним.")
    if n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    print("=" * 50)
    print("Програма розрахунку чисел Фібоначчі")
    print("=" * 50)
    try:
        num = int(input("Введіть порядковий номер n: "))
        result = fibonacci(num)
        print(f"\n[Результат] F({num}) = {result}")
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()