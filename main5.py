def solve():
    try:
        # Зчитуємо довжину послідовності n
        n_input = input("Введіть довжину послідовності n: ")
        n = int(n_input.strip())
        
        # Визначаємо модуль для обчислень
        MOD = 12345
        
        # Перевірка базових випадків
        if n <= 0:
            print(0)
            return
        elif n == 1:
            print(2)
            return
        elif n == 2:
            print(4)
            return
        elif n == 3:
            print(7)
            return
        
        # Виділяємо пам'ять під масив для динамічного програмування
        dp = [0] * (n + 1)
        dp[1] = 2
        dp[2] = 4
        dp[3] = 7
        
        # Обчислюємо значення за формулою Tribonacci з модулем
        for i in range(4, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
            
        print(f"Кількість шуканих послідовностей: {dp[n]}")
        
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

if __name__ == "__main__":
    solve()