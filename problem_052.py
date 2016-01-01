# coding: utf-8


'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''


def get_digits(number):
    return sorted(str(number))


def same_digits(number):
    digits = get_digits(number)
    for multiple in range(6, 2, -1):
        if get_digits(multiple * number) != digits:
            return False
    return True


def main():
    number = 10
    while 1:
        str_number = str(number)
        if str_number[0] != '1':
            number += 8 * 10 ** (len(str(number)) - 1)
        if str_number[1] not in ['1', '2', '3', '4', '5', '6']:
            number += 1
        # digits = get_digits(number)
        # if all([digits == get_digits(multiple) for multiple in [6 * number, 5 * number, 4 * number, 3 * number, 2 * number]]):
        if same_digits(number):
            return number
        number += 1


if __name__ == '__main__':
    print(main())
    # 142857 in 201ms
