# Завдання 1.2  Програмно побудуйте бінарне дереву пошуку, послідовно вставляючи 
# елементи: 60, 40, 80, 20, 50, 70, 90, 10 

#клас вузла дерева
#клас вузла дерева
class Node:
    def __init__(self, data):
        self.data = data # дані, які зберігає вузол (ключ BST)
        self.left = None  # посилання на менші значення (лівий нащадок)
        self.right = None # посилання на більші значення (правий нащадок)
        
# клас бінарного дерева пошуку (BST)
class BST:
    def __init__(self):
        self.root = None #вказує на кореневий вузол (початок структури)
    
    #функція для вставки елемента (використовуємо дл для побудови дерева)
    def insert(self, data):
        new_node = Node(data)
        
        #якщо дерево порожнє
        if self.root is None:
            self.root = new_node
            return
        #якщо пошук місця для вставки (ітеративно)
        current = self.root #починаємо з кореня
        while True:
            #рух вліво (якщо нове значення data менше за поточний вузол current.data)
            if data < current.data: 
                if current.left is None:
                    current.left = new_node #вставка тут - новий вузол new_node стає нащадком  
                    return
                current = current.left #пересуваємося вліво
            #рух вправо (якщо нове значення data > значення поточного вузла current.data)
            elif data > current.data:
                if current.right is None: #знайшли місце вставки
                    current.right = new_node 
                    return
                current = current.right #пересуваємося вправо
            else:               
                return  #елемент вже існує (дублікати ігноруються)


bst_tree = BST()
elements = [60, 40, 80, 20, 50, 70, 90, 10]
print(f"Вставка заданих елементів: {elements}")

for elem in elements:
    bst_tree.insert(elem)
    
