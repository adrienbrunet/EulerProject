# coding: utf-8

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


from itertools import count, islice
from math import sqrt
import operator


'''
method: divisible by all numbers from 1 to 20 --> max = 20
We search for all prime factor below 20.
For each of them, we take its biggest power below the max.
We make the product of all this numbers.
max = 10 --> prime numbers: 2, 3, 5, 7 --> max from prime numbers: 8, 9, 5, 7
product: 2520
'''


def is_divisible_by_all_int_up_to(number, _max):
    return all(number % i == 0 for i in range(1, _max + 1))


def is_prime(number):
    '''Check if the number is a prime number'''
    if number < 2:
        return False
    return all(number % i for i in islice(count(2), int(sqrt(number) - 1)))


def list_prime_under(number):
    return [i for i in range(number + 1) if is_prime(i)]


def get_max_power_below(_max, prime):
    power = 1
    while prime ** power < _max:
        max_power = prime ** power
        power += 1
    return max_power


def product(_max):
    _list_factor = []
    _list = list_prime_under(_max)
    for prime in _list:
        _list_factor.append(get_max_power_below(_max, prime))
    return reduce(operator.mul, _list_factor, 1)


def test_is_divisible_by_all_int_up_to():
    assert is_divisible_by_all_int_up_to(2520, 10)


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(23)


def test_list_prime_under():
    assert list_prime_under(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_get_max_power_below():
    assert get_max_power_below(10, 2) == 8


def test_product():
    assert product(10) == 2520


test_is_prime()
test_is_divisible_by_all_int_up_to()
test_list_prime_under()
test_get_max_power_below()
test_product()

print product(20)
