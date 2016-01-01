# coding: utf-8

'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle        Tn=n(n+1)/2         1, 3, 6, 10, 15, ...
Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

# if we generate the hexagonal number, we see that every hexagonal number
# is a triangle number
# Indeed, with n = 2_n - 1, an hexagonal number Hn is triangle Tn.
# We just need a triangle number which is also a pentagonal one


import math


def is_pentagonal(number):
    return not (math.sqrt(1 + 24 * number) + 1) % 6


def main():
    n = 143
    number = 0
    while not is_pentagonal(number):
        n += 1
        number = n * (2 * n - 1)

    return number


if __name__ == '__main__':
    print(main())
    # 1533776805 in 20mms
