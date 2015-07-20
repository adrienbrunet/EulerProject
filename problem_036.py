# coding: utf-8

'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''


def reverse_int(number):
    return int(str(number)[::-1])


def reverse_int_b(number):
    number = str(number)[2:]
    return int('0b' + str(number)[::-1], 2)


def is_a_palindrome(number):
    return reverse_int(number) == number


def is_a_palindrome_b(number):
    return reverse_int_b(number) == int(number, 2)


def test_reverse_int():
    assert reverse_int(1234) == 4321


def test_is_a_palindrome():
    assert is_a_palindrome(123454321)
    assert not is_a_palindrome(12345)


def result():
    _list = []
    for i in range(1, 1000000, 2):
        if is_a_palindrome(i):
            if is_a_palindrome_b(bin(i)):
                _list.append(i)
    return sum(_list)


if __name__ == '__main__':
    print(result())
    # 872187
