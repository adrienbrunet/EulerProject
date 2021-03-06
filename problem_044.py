# coding: utf-8

'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''


import math


def is_pentagonal(number):
    return not (math.sqrt(1 + 24 * number) + 1) % 6


def main():
    j = 1
    while 1:
        j += 1

        # pentagonal number
        n = j * (3 * j - 1) // 2

        for k in range(j - 1, 0, -1):
            m = k * (3 * k - 1) // 2
            if (is_pentagonal(n - m) and is_pentagonal(n + m)):
                return n - m


if __name__ == '__main__':
    print(main())
    # 5482660 in 1.86s
