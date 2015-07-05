# coding: utf-8


'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


''' Ran in 22 sec... Should be optimized...'''


from itertools import count, islice
from math import sqrt


def is_prime(number):
    '''Check if the number is a prime number'''
    if number < 2:
        return False
    return all(number % i for i in islice(count(2), int(sqrt(number) - 1)))


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(23)


def result(_max):
    list_prime = [i for i in range(_max) if is_prime(i)]
    return sum(list_prime)


def test_result():
    assert result(10) == 17


test_result()
print result(2000000)
