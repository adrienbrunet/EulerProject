# coding: utf-8

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''


from itertools import chain, cycle, accumulate  # accumuate, python3 only

from helpers import is_prime


def result():
    nb_prime = 0
    for i in accumulate(chain([2, 1, 2], cycle([2, 4]))):
        if is_prime(i):
            nb_prime += 1
        if nb_prime == 10001:
            return i


if __name__ == '__main__':
    print(result())
    # 104743
