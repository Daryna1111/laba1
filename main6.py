import math

def main():
    try:
        # Зчитуємо чотири координати x1, y1, x2, y2 з одного рядка
        input_data = input()
        x1, y1, x2, y2 = map(float, input_data.split())
        
        # Обчислюємо довжину вектора
        length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # Виводимо результат з точністю до 6 знаків після коми
        print(f"{length:.6f}")
        
    except ValueError:
        print("Будь ласка, введіть чотири числа через пробіл.")

if __name__ == "__main__":
    main()