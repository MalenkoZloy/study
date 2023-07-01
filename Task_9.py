def image_info(**my_dict):
    if 'image_id' not in my_dict:
        raise TypeError("Ключа: image_id нет в словаре!")
    elif 'image_title' not in my_dict:
        raise TypeError("Ключа: image_title нет в словаре")
    return f"Image {my_dict['image_title']} has id {my_dict['image_id']}"


try:
    my_info = {
        'image_title': 'my cat',
        'image_id': 5136
    }
    result = image_info(**my_info)
    print(result)
except Exception as e:
    print(e)
