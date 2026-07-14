def solve():
    try:
        # Зчитуємо кількість розрядів p
        p = int(input().strip())
        
        # Перевірка базових випадків
        if p <= 0:
            print(0)
            return
        elif p == 1:
            print(2)
            return
        elif p == 2:
            print(4)
            return
        
        # Динамічне програмування для p > 2
        dp = [0] * (p + 1)
        dp[1] = 2
        dp[2] = 4
        
        for i in range(3, p + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        print(dp[p])
        
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

if __name__ == "__main__":
    solve()