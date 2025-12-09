# kr1_sorting_task_5_3.py
#Завдання 5.3: Реалізуйте 2 алгоритми сортування на вибір. Проведіть трасування
#(покрокове виконання) для масиву: [8, 4, 7, 2]. Поясніть, чим ці методи
#відрізняються з точки зору кількості обмінів. 


# 5.3.1 Реалізація сортування бульбашкою
#O(N^2) у найгіршому випадку

def bubble_sort(arr: list) -> list:
    n = len(arr)
    swaps_count = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # обмін 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swaps_count += 1
        if not swapped:
            break
    return arr, swaps_count #повертаємо масив і кількість обмінів

# 5.3.2 Реалізація швидкого сортування 
# не in-place, прямі обміни не відбуваються
# O(N log N) у середньому випадку
def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quick_sort(less) + equal + quick_sort(greater)

# -------------------------------------------

#вхідні дані для трасування
A_input = [8, 4, 7, 2]
A_expected = [2, 4, 7, 8]

print("\n**** ТЕСТУВАННЯ ЗАВДАННЯ 5.3: СОРТУВАННЯ ТА ОБМІНИ ****")
print(f"Вхідний масив: {A_input}")
print(f"* Очікуваний результат: {A_expected} *")

#BUBBLE SORT
#необхідно створити копію масиву для тестування in-place сортування
A_bubble = A_input[:] 
A_sorted_bubble, swaps_bubble = bubble_sort(A_bubble)

print("\nТЕСТ 1: Сортування Бульбашкою")
print(f"Фактичний результат сортування: {A_sorted_bubble}")

if A_sorted_bubble == A_expected:
    print("Тест 1.1: успіх (Масив коректно відсортований).")
else:
    print("Тест 1.1: невдача (Масив не відсортований).")

print(f"Фактична кількість обмінів (трасування): {swaps_bubble}") # Очікувано: 5
if swaps_bubble == 5:
    print("Тест 1.2: успіх (Кількість обмінів відповідає трасуванню).")
else:
    print("Тест 1.2: невдача (Кількість обмінів не відповідає).")

#QUICK SORT
A_quick = A_input[:]
A_sorted_quick = quick_sort(A_quick)
swaps_quick = 0 # у цій реалізації обміни на місці не відбуваються

print("\nТЕСТ 2: Швидке Сортування")
print(f"Фактичний результат сортування: {A_sorted_quick}")

if A_sorted_quick == A_expected:
    print("Тест 2.1: успіх (масив відсортований)")
else:
    print("Тест 2.1: невдача (масив не відсортований)")

print(f"Фактична кількість прямих обмінів (трасування): {swaps_quick}") # 0
print("Висновок 2.2: успіх (Кількість прямих обмінів 0, оскільки використано копіювання).")