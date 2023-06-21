def print_number_info(num):
    if (num % 2) == 0:
        print("Entered numbers is even")
    else:
        print("Entered numbers is odd")


def test_info(num):
    print("Square of the num is", num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input("Enter any number: "))

process_number(entered_num, print_number_info)
process_number(entered_num, test_info)

"""
1. def print_number_info(num): объявляет функцию print_number_info, которая принимает один аргумент num.
2. if (num % 2) == 0: проверяет, является ли num четным числом, используя оператор остатка от деления (%).
3. print("Entered numbers is even") выводит сообщение "Entered numbers is even", если num четное.
4. else: Если num не четное, то выполнится следующая строка.
5. print("Entered numbers is odd") выводит сообщение "Entered numbers is odd", если num нечетное.
6. def process_number(num, callback_fn): объявляет функцию process_number, которая принимает два аргумента: num и callback_fn.
7. callback_fn(num) вызывает функцию обратного вызова, переданную в качестве аргумента callback_fn с аргументом num.
8. entered_num = int(input("Enter any number: ")) запрашивает у пользователя ввод числа и сохраняет его в переменной entered_num.
9. process_number(entered_num, print_number_info) вызывает функцию process_number, передавая ей введенное пользователем число и функцию print_number_info в качестве функции обратного вызова. 
В итоге, программа проверяет, является ли введенное пользователем число четным или нечетным, используя функцию print_number_info, которая вызывается через функцию обратного вызова process_number.
"""