# Задача 5
# 1. Создайте функцию merge_lists_to_dict
# 2. У функции должно быть два параметра
# 3. Функция должна объединять два списка, используя встроенную функцию zip
# 4. Конвертируйте объект zір в словарь и верните его из функции
# 5. Вызовите функцию, передав ей два списка в качестве аргументов
# 6. Выведите результат вызова функции в терминал

def merge_lists_to_dict(list1, list2):
    my_dict = []
    my_dict = dict(zip(list1, list2))
    return my_dict


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(merge_lists_to_dict(list1, list2))
