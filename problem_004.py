# coding: utf-8

'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


from itertools import combinations_with_replacement


def is_a_palindrome(number):
    _number = str(number)
    return _number[::-1] == _number


def test_is_a_palindrome():
    assert is_a_palindrome(123454321)
    assert not is_a_palindrome(12345)


def list_product_3_digit():
    ''' return a list of 3digit product, in a descending order'''
    _ = [a * b for (a, b) in combinations_with_replacement(range(100, 1000), 2)][::-1]
    _.sort(reverse=True)
    return _


def result():
    for _product in list_product_3_digit():
        if is_a_palindrome(_product):
            return _product


def main():
    return result()


if __name__ == '__main__':
    test_is_a_palindrome()
    print(main())
    # 906609 return in 250ms
