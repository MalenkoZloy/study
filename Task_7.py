# Задача 7
# 1. Создайте функцию update_car_info, в которой все именованные аргументы будут объединяться в словарь car
# 2. Добавьте в словарь новый ключ is available c значением True
# 3. Верните из функции изменённый словарь
# 4. Вызовите функцию с именованными аргументами brand и price, их значения могут быть любыми
# 5. Выведите в терминал результат функции

def update_car_info(**car):  # 1
    car_info = car  # 1
    car['is available'] = True  # 2
    return car_info  # 3


car_info = update_car_info(brand='Ford', price=120000)  # 4
print(car_info)  # 5
