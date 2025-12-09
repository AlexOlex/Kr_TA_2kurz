# Завдання 5.1. Реалізуйте лінійний пошук повним перебором елементів у масиві та 
# двійковий пошук. Для кожної функції вкажіть її найгіршу часову 
# складність у О-нотації. 

# лінійний пошук повним перебором
# найгірша часова складність: O(N)
# N - кількість елементів у масиві
def linear_search(arr: list, target) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # елемент знайдено
    return -1  #елемент не знайдено

# бінарний пошук
# вимагає щоб масив arr був відсортований
# найгірша часова складність O(log N)
def binary_search(arr: list, target) -> int:
   
    low = 0
    high = len(arr) - 1

    while low <= high:
        # обчислення середнього індексу
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid  #елемент знайдено
        elif arr[mid] < target:
            low = mid + 1  #шукаємо у правій половині
        else:
            high = mid - 1 #шукаємо у лівій половині
            
    return -1 #елемент не знайдено

#-------------------------------------------------------

A_unsorted = [3, 5, 1, 17, 11, 13, 7]
A_sorted = [1, 3, 5, 7, 11, 13, 17]

print("\nТЕСТУВАННЯ ЗАВДАННЯ 5.1 КР 1 Лінійний і бінарний пошук")

#ЛІНІЙНИЙ ПОШУК
print("\n* Лінійний пошук (O(N)) *")
print(f"массив: {A_unsorted}")

# пошук успішний (знайдено 7)
result_7_linear = linear_search(A_unsorted, 7)
print(f"пошук 7: індекс {result_7_linear}") # 6

# пошук неуспішний (не знайдено 2)
result_2_linear = linear_search(A_unsorted, 2)
# Вивід: -1
print(f"пошук 2: індекс {result_2_linear}") 

#ДВІЙКОВИЙ ПОШУК
print("\n* Двійковий пошук (O(log N)) *")
print(f"масив: {A_sorted}")

# пошук успішний (знайдено 7)
result_7_binary = binary_search(A_sorted, 7)
print(f"пошук 7: індекс {result_7_binary}") # 3

# пошук неуспішний (не знайдено 2)
result_2_binary = binary_search(A_sorted, 2)

#вивід з поясненням спеціального значення -1
if result_2_binary == -1:
    print(f"пошук 2: індекс {result_2_binary} (спеціальне значення, оскільки елемент не знайдено)")
else:
    print(f"пошук 2: індекс {result_2_binary}")