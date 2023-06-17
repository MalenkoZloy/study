# Задача 6
# 1. Перепишите вызов функции merge_lists to dict из предыдущей задачи так, чтобы в нём использовались аргументы с
# ключевыми словами
# 2. Добавьте ещё один вызов функции, в котором будет один позиционный аргумент, а второй -
# # аргумент с ключевым словом


def merge_lists_to_dict(name, age):  # 1
    info = f"{name} is {age} years old"  # 1
    return info  # 1


print(merge_lists_to_dict(name='Ivan', age=25))  # 1
print(merge_lists_to_dict('Jon', age=25))  # 2
