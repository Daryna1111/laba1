import math
from collections import Counter

def solve():
    try:
        # Зчитуємо слово та прибираємо зайві пробіли на початку чи в кінці
        word = input("Введіть слово: ").strip()
        
        if not word:
            print("Рядок порожній.")
            return
        
        # Переводимо у верхній регістр, щоб регістр не впливав на підрахунок букв (як у прикладі SoLo -> 12)
        word_upper = word.upper()
        
        n = len(word_upper)
        
        # Рахуємо частоту появи кожної букви у слові
        letter_counts = Counter(word_upper)
        
        # Обчислюємо чисельник: N!
        numerator = math.factorial(n)
        
        # Обчислюємо знаменник: добуток факторіалів кількостей кожної букви
        denominator = 1
        for count in letter_counts.values():
            denominator *= math.factorial(count)
            
        # Рахуємо фінальну кількість унікальних анаграм
        anagrams_count = numerator // denominator
        
        print(f"Кількість анаграм: {anagrams_count}")
        
    except Exception as e:
        print("Виникла помилка під час обчислень.")

if __name__ == "__main__":
    solve()