# coding: utf-8

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


from functools import reduce
from operator import mul

from helpers import eratosthene


'''
method: divisible by all numbers from 1 to 20 --> max = 20
We search for all prime factors below 20 and take their biggest power below max.
We make the product of all this factors.
max = 10 --> prime numbers: 2, 3, 5, 7 --> max from prime numbers: 8, 9, 5, 7
product: 2520
'''


def is_divisible_by_all_int_up_to(number, _max):
    return all(number % i == 0 for i in range(1, _max + 1))


def get_max_power_below(_max, prime):
    power = 1
    while prime ** power < _max:
        max_power = prime ** power
        power += 1
    return max_power


def product(_max):
    _list_factor = [get_max_power_below(_max, prime) for prime in eratosthene(_max)]
    return reduce(mul, _list_factor, 1)


def test_is_divisible_by_all_int_up_to():
    assert is_divisible_by_all_int_up_to(2520, 10)


def test_get_max_power_below():
    assert get_max_power_below(10, 2) == 8


def test_product():
    assert product(10) == 2520


def main():
    return product(20)


if __name__ == '__main__':
    test_is_divisible_by_all_int_up_to()
    test_get_max_power_below()
    test_product()

    print(main())
    # 232792560 in 23.7usec
