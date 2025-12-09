#kr1_hash_table_collision_resolve_task_6_2.py
#Завдання 6.2:  Опишіть структуру Хеш-таблиці. Реалізуйте клас HashTable 
#з хеш функцією та механізмом вирішення колізій,
# наприклад за допомогою методу ланцюжків. 


class HashTable:
    def __init__(self, size):
        #ініціалізація хеш-таблиці розміру M
        self.size = size
        #кожна корзина ініціалізується порожнім списком (ланцюжком)
        self.table = [[] for _ in range(self.size)]
    #внутрішня хеш-функція (використовує метод залишку від ділення)
    def _hash(self, key):
        if isinstance(key, str):
            hash_value = sum(ord(char) for char in key)
        else:
            hash_value = key
        
        return hash_value % self.size
    #додає або оновлює пару ключ-значення з обробкою колізій
    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        
        #пошук та оновлення
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        #додавання нового елемента (колізія або новий ключ)
        bucket.append((key, value))
    #отримує значення за ключем
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"ключ '{key}' не знайдено")
    #видаляє пару ключ-значення за ключем
    def delete(self, key):
        
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        
        raise KeyError(f"ключ '{key}' не знайдено")
        
#Тестування --------------------------------------        

M = 7
ht = HashTable(size=M)
print(f"\n*** ТЕСТУВАННЯ HashTable (M={M}) *****")

#вставка та колізія ( 13, 41 обидва дають індекс 6)
ht.insert(13, 'Клієнт_13')      
ht.insert(41, 'Клієнт_41')      
ht.insert('Tiger', 515)    # 'Tiger' (507) mod 7 = 3

print("1-2. Таблиці після перших вставок:")
# Очікується: T[3] = [('Tiger', 515)]; T[6] = [(13, 'Клієнт_13'), (41, 'Клієнт_41')]
print(f"       {ht.table}")

#оновлення та пошук
# Значення для 13 оновлено на 'Оновлено' (як у попередньому кроці)
ht.insert(13, 'Оновлено')
print(f"3. Значення для 13 після оновлення: {ht.get(13)}")

#пошук елемента в ланцюжку (41)
print(f"4. Значення для 41: {ht.get(41)}")

#видалення
ht.delete(41)
print(f"5. Ланцюжок після видалення 41 (Індекс 6): {ht.table[6]}")

#виняток
try:
    ht.get(41)
except KeyError as e:
    print(f"6. Спроба пошуку 41: {e}")
        
        