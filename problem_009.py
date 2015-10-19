# coding: utf-8

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


from math import sqrt


def main():
    first_1000_square = [i ** 2 for i in range(1, 1000)]
    for (counter, i) in enumerate(first_1000_square):
        for j in first_1000_square[counter + 1:]:
            if i + j in first_1000_square and sqrt(i) + sqrt(j) + sqrt(i + j) == 1000:
                return int(sqrt(i) * sqrt(j) * sqrt(i + j))


if __name__ == '__main__':
    print(main())
    # 31875000
