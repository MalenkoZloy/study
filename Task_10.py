box = {'speed': 55.123, 'time': 100.500}


def route_info(**new_box):
    if 'distance' in new_box:
        distance = new_box['distance']
        if distance % 1 == 0:
            return f"Все ок, вот тебе дистанция: {distance}"
        else:
            return f"{distance} является не целочисленным числом"

    elif 'speed' and 'time' in new_box:
        speed = new_box['speed']
        time = new_box['time']
        if speed % 1 == 0 and time % 1 == 0:
            return f"Нет дистанции,но есть {speed * time}"
        elif speed % 1 != 0 and time % 1 != 0:
            return f"{speed} и {time} не целочисленные числа"
        elif speed % 1 != 0:
            return f"{speed} является не целочисленным числом"
        elif time % 1 != 0:
            return f"{time} является не целочисленным числом"

    else:
        return f"Нет вообще ничего!"


print(route_info(**box))
