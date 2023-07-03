"""
Задача 9
1. Создайте функцию image info с одним параметром типа dict
2. Функция ожидает словарь, в котором должно быть как минимум два ключа:
• image_id
• image_title
3. Функция должна возвращать строку такого вида
"Image 'my cat' has id 5136"
4. Если хотя бы одного из этих ключей в словаре нет, функция должна генерировать ошибку TypeError
5. Вызовите функцию и корректно обработайте ошибку в случае возникновения
"""


def image_info(**my_dict): 
    if 'image_id' not in my_dict and 'image_title' not in my_dict:
        raise TypeError("Ключа images_title и image_id нет в словаре")
    elif 'image_title' not in my_dict:
        raise TypeError("Ключа: image_title нет в словаре")
    elif 'image_id' not in my_dict:
        raise TypeError("Ключа: image_id нет в словаре!")
    return f"Image {my_dict['image_title']} has id {my_dict['image_id']}"
    
        


try:
    my_info = {
        'image_titl': 'my cat',
        'image_i': 5136
    }
    result = image_info(**my_info)
    print(result)
except Exception as e:
    print(e)
