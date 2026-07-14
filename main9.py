import math

def solve():
    try:
        # Зчитуємо x та y
        line = input().strip()
        if not line:
            return
        
        x, y = map(int, line.split())
        
        # Обчислюємо відстань
        d = y - x
        
        if d < 0:
            print("Помилка: x має бути меншим або дорівнювати y.")
            return
        elif d == 0:
            print(0)
            return
            
        # Знаходимо цілу частину квадратного кореня з відстані
        m = int(math.isqrt(d))
        
        # Визначаємо кількість кроків за формулою
        if d == m * m:
            steps = 2 * m - 1
        elif d <= m * m + m:
            steps = 2 * m
        else:
            steps = 2 * m + 1
            
        print(steps)
        
    except ValueError:
        print("Будь ласка, введіть два цілих числа через пробіл.")

if __name__ == "__main__":
    solve()