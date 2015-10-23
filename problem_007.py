# coding: utf-8

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''


from itertools import islice  # accumuate, python3 only

from helpers import eratosthene


def main():
    return next(islice(eratosthene(105000), 10000, 10000 + 1))


if __name__ == '__main__':
    print(main())
    # 104743 in 5ms
