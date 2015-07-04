# coding: utf-8

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from itertools import count, islice
from math import sqrt


def is_prime(number):
    '''Check if the number is a prime number'''
    if number < 2:
        return False
    return all(number % i for i in islice(count(2), int(sqrt(number) - 1)))


def list_factor(number):
    ''' Give the list of factor of a given number'''
    return set([j for i in range(1, int(sqrt(number)) + 1) for j in [i, number // i] if number % i == 0])


def prime_factor(number):
    ''' returns the set of prime factor among the factor of the number'''
    return set([i for i in list_factor(number) if is_prime(i)])


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(23)


def test_list_factor():
    assert list_factor(20) == {1, 20, 2, 10, 4, 5}


def test_prime_factor():
    assert prime_factor(13195) == {5, 7, 13, 29}


test_is_prime()
test_list_factor()
test_prime_factor()

list_prime_factor = list(prime_factor(600851475143))
list_prime_factor.sort()
print list_prime_factor[-1]
