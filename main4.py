def solve():
    try:
        # Зчитуємо натуральне число n
        n_input = input("Введіть натуральне число n: ")
        n = int(n_input.strip())
        
        if n <= 1:
            print(0)
            return
            
        count = 0
        k = 1
        
        # Шукаємо дільники k, що задовольняють умову k * (k + 1) < n
        while k * (k + 1) < n:
            if n % k == 0:
                count += 1
            k += 1
            
        print(f"Кількість рівних дільників числа {n}: {count}")
        
    except ValueError:
        print("Будь ласка, введіть коректне натуральне число.")

if __name__ == "__main__":
    solve()