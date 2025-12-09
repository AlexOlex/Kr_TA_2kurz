# Завдання 3.4.1. Функцію, яка приймає рядок тексту і повертає словник, 
# де ключами є слова з тексту, а значеннями  -  їхня частота появи
def get_word_freq(text: str) -> dict:
  
    import string
    
    low = text.lower()  # до нижнього регістру
    
    # str.maketrans('', '', string.punctuation) створює таблицю
    # яка відображає кожен знак пунктуації на None (=видаляє)
    cleaned = low.translate(str.maketrans('', '', string.punctuation))
    
    # split() без аргументів розділяє тексту на список слів 
    # по будь-якому пробільному символу і відкидає порожні рядки
    words = cleaned.split()
    
    freq_in_dict = {}
    
    for word in words:
        # якщо 'word' є в словнику, беремо його значення; інакше беремо 0
        freq_in_dict[word] = freq_in_dict.get(word, 0) + 1
                
    return freq_in_dict


text = "The, Cat, sits, on, a, mat, and the cat is happy on the mat."
freq = get_word_freq(text)

print(f"Заданий текст:\n'{text}'")
print("\nСловник частоти слів:")
print(freq)

print(f"частота слова 'cat': {freq.get('cat')}")
print(f"частота слова 'the': {freq.get('the')}")
print(f"частота слова 'dog': {freq.get('dog')}")


