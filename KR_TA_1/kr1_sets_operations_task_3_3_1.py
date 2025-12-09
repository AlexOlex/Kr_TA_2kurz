# kr1_sets_operations_task_3_3_1.py
#Завдання 3.3.1 Операції над множинами

print("\n * Завдання 3.3.1 Операції над множинами *")
print()

set_A = {1, 3, 5, 7, 11, 13}
set_B = {5, 7, 11, 13, 17, 19}

print(f"множина A: {set_A}")
print(f"множина B: {set_B}")

# Об'єднання, оператор |
#всі унікальні елементи, які є в A АБО в B.
union = set_A | set_B
print("\nОб'єднання")
print(f"(A | B): {union}")


# Перетин, оператор &
# всі елементи, що є в A І в B
intersect = set_A & set_B
print("\nПеретин")
print(f"(A & B): {intersect}")


# Різниця, оператор -
# всі елементи, які є в A, але немає в B
diff = set_A - set_B
print("\nРізниця)")
print(f"(A - B): {diff}")


# для порівняння різниця (B - A)  
diff_B_A = set_B - set_A
print(f"(B - A): {diff_B_A}")

# Симетрична різниця, оператор ^
# елементи, які є в A АБО в B, але не в обох (унікальні для кожної множини).
sym_diff = set_A ^ set_B
print("\nСиметрична різниця")
print(f"(A ^ B): {sym_diff}")
