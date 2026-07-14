import math
from functools import reduce

def lcm_of_two(a, b):
    """Функція для обчислення НСК двох чисел"""
    return abs(a * b) // math.gcd(a, b)

def main():
    try:
        # Зчитуємо перший рядок: кількість чисел p
        p_input = input()
        p = int(p_input.strip())
        
        # Зчитуємо другий рядок: самі числа, розділені пробілом
        numbers_input = input()
        numbers = list(map(int, numbers_input.split()))
        
        # Перевірка: чи збігається реальна кількість чисел із заданим p
        if len(numbers) != p:
            # Якщо ввели іншу кількість, використовуємо лише перші p чисел
            numbers = numbers[:p]
            
        # Обчислюємо НСК для всього списку чисел
        result = reduce(lcm_of_two, numbers)
        
        # Виводимо результат
        print(result)
        
    except (ValueError, IndexError):
        print("Помилка введення даних. Будь ласка, перевірте формат.")

if __name__ == "__main__":
    main()