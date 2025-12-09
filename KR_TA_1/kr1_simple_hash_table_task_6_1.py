#kr1_simple_hash_table_task_6_1.py
#Завдання 6.1 Реалізуйте просту хеш-функцію (наприклад, залишок від ділення).

# h(k) = k mod M
def simple_hash_func(key, table_size):
    """
    Реалізація хеш-функції методом залишку від ділення.
    """
    if isinstance(key, str):
        # перетворення рядка на числове значення
        hash_value = sum(ord(char) for char in key)
    else:
        # використання числового ключа
        hash_value = key
        
    # обчислення індексу
    return hash_value % table_size

# Тестування 
M = 7  # розмір таблиці
# ASCII 65 
test_keys = [13, 17, 7, 41, 53, 'A'] # 'A' = ASCII 65 

print(f"Тест 6.1 (M={M})")
for key in test_keys:
    index = simple_hash_func(key, M)
    
    if isinstance(key, str):
        hash_value = sum(ord(char) for char in key)
        print(f"ключ '{key}': [хеш-індекс = {index} ({hash_value} mod {M} = {index})")
    else:
        print(f"ключ {key}: [хеш-індекс = {index} ({key} mod {M} = {index})")