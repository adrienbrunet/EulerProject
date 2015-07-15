# coding: utf-8

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


def reverse_int(number):
    return int(str(number)[::-1])


def is_a_palindrome(number):
    return reverse_int(number) == number


def test_reverse_int():
    assert reverse_int(1234) == 4321


def test_is_a_palindrome():
    assert is_a_palindrome(123454321)
    assert not is_a_palindrome(12345)


def list_product_3_digit():
    ''' return a list of 3digit product, in a descending order'''
    _list = sorted(set(i * j for i in range(100, 1000) for j in range(100, 1000)), reverse=True)
    return _list


def result():
    for _product in list_product_3_digit():
        if is_a_palindrome(_product):
            return _product


if __name__ == '__main__':
    test_reverse_int()
    test_is_a_palindrome()
    print(result())
    # 906609
