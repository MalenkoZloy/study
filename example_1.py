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