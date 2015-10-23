# coding: utf-8

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a ** 2 + b ** 2 = c ** 2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


from math import sqrt
from itertools import combinations


def main():
    for (i, j) in combinations(range(1, 1001), 2):
        k = sqrt(i ** 2 + j ** 2)
        if i + j + k == 1000 and (k - int(k)) == 0:
            return i * j * int(k)


if __name__ == '__main__':
    print(main())
    # 31875000 in 150ms
