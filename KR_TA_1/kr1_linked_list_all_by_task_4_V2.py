# kr1_linked_list_all_by_task_4_V2.py
# Завдання 4.2. Опис клас Node і LinkedList.
# Завдання 4.3. Метод insert_at_end(data) для додавання елемента в кінець однозв'язного списку (SLL). 
# Завдання 4.5 a) Додавання елемента в початок списку 
# Завдання 4.5 d) Видалення елемента з початку списку

# Завдання 4.2. Опис класу Node (Вузол)
class Node:
    # окремий вузол у зв'язному списку, містить дані та посилання на наступний вузол
    def __init__(self, data):
        # дані, які зберігає вузол
        self.data = data
        # посилання на наступний вузол у списку (спочатку None)
        self.next = None

# Завдання 4.2. Опис класу LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
    # Завдання 4.4.   
    # метод insert_at_end(data) для додавання елемента в кінець однозв'язного списку (SLL)
    def print_list(self):
        current_node = self.head  #починаємо з голови
        output = ""
        while current_node:
            # додаємо дані поточного вузла до рядка виводу
            output += str(current_node.data) + " -> "
            # переход до наступного вузла
            current_node = current_node.next
            
        # виводимо весь рядок (останнє -> замінено на None)
        print(output + "None")

    # Завдання 4.3.
    # метод insert_at_end(data) додає новий вузол з data в кінець списку
    # складність O(N)
    def insert_at_end(self, data):
      
        new_node = Node(data)
        
        # якщо список порожній, новий вузол стає головою
        if self.head is None:
            self.head = new_node
            return
            
        #знаходимо останній вузол
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        # встановлюємо посилання next останнього вузла на новий вузол
        last_node.next = new_node
        
    # Завдання 4.5. a) Додавання елемента в початок списку ()       
    # складність O(1)
    # новий вузол з data додається на початок списку і стає його новою головою
    def insert_at_start(self, data):
       
        new_node = Node(data)
        
        # новий вузол на поточну голову списку
        new_node.next = self.head
        
        # новий вузол -> нова головою
        self.head = new_node   
        
        # Завдання 4.5. d) Видалення елемента з початку списку       
        # складність O(1)
        # видаляє головний вузол списку (head) і робить наступний вузол новою головою
    def delete_from_start(self):
        # випадок якщо список порожній
        if self.head is None:
            print("! Список порожній")
            return
        # випадок якщо список має елементи
        #зберігаємо посилання на вузол, який ми хочемо видалити
        deleted_node = self.head
        deleted_data = deleted_node.data
        #пересуваємо покажчик голови на наступний вузол
        self.head = self.head.next
        #додатково (для очищення пам'яті) розриваємо зв'язок зі старим вузлом
        deleted_node.next = None
        
        print(f"видалено такий елемент з початку списку: {deleted_data}")
        return deleted_data       
        
        

my_list = LinkedList()

print("\n***** ТЕСТУВАННЯ ЗАВДАННЯ 4 КР1 Зв'язний список *****")
print()

# Тест 4.3 (insert_at_end 11, 13, 17)
# 11 -> 13 -> 17
my_list.insert_at_end(11)
my_list.insert_at_end(13)
my_list.insert_at_end(17)
print("\n* ОЧІКУВАНО: 11 -> 13 -> 17 -> None *")
print("ОТРИМАНО після 3x insert_at_end(11, 13, 17):")
my_list.print_list()

# Тест 4.5 a) (insert_at_start 7)
# 7 -> 11 -> 13 -> 17
my_list.insert_at_start(7)
print("\n* ОЧІКУВАНО: 7 -> 11 -> 13 -> 17 -> None *")
print("ОТРИМАНО після insert_at_start(7):")
my_list.print_list()

# Тест 4.5 a) (insert_at_start 5)
# 5 -> 7 -> 11 -> 13 -> 17
my_list.insert_at_start(5)
print("\n* ОЧІКУВАНО: 5 -> 7 -> 11 -> 13 -> 17 -> None *")
print("ОТРИМАНО після insert_at_start(5) (нова голова):")
my_list.print_list()


# Тест 4.5 d) (delete_from_start 5)
# 7 -> 11 -> 13 -> 17
deleted = my_list.delete_from_start() # видалено 5

print("\n* ОЧІКУВАНО: 7 -> 11 -> 13 -> 17 -> None *")
print("ОТРИМАНО після delete_from_start() (видалено 5):")
my_list.print_list()

# Тест 4.5 d) (delete_from_start 7)
# 11 -> 13 -> 17
deleted = my_list.delete_from_start() # видалено 7

print("\n* ОЧІКУВАНО: 11 -> 13 -> 17 -> None *")
print("ОТРИМАНО після delete_from_start() (видалено 7):")
my_list.print_list()  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        