# Задача 4
# 1. Создайте набор с нескольких элементов типа int
# 2. Добавьте в него ещё один элемент
# 3. Создайте ещё один набор с несколькими элементами, причём некоторые должны быть такими же как в первом наборе
# 4. Найдите общие элементы в двух наборах и поместите их в новый набор
# 5. Конвертируйте результирующий набор в список и выведите список в терминал

my_set = {12, 5, 1993}  # 1
my_set.add('may')  # 2
my_set_clone = my_set.copy()  # 3
my_set_clone.add('DevOps')  # 3


new_set = my_set & my_set_clone  # 4
print(list(new_set))  # 5