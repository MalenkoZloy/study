button = {
    'name': 'Ivan',
    'year': 30
}

new_button = {
    **button,
    'man': True
}

print(button)
print(new_button)
#  Благодаря ** можно распаковать словарь button в новый словарь
