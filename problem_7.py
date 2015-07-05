# coding: utf-8

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

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


i = 1
nb_prime = 0
while nb_prime != 10001:
    if is_prime(i):
        nb_prime += 1
    i += 1

print i - 1
