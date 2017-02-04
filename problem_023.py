# coding: utf-8

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from itertools import combinations_with_replacement

from helpers import factors


upper_limit = 28124


def main():
    numbers_to_upper_limit = range(upper_limit)
    abundant_numbers = [nb for nb in numbers_to_upper_limit if sum(factors(nb)) > 2 * nb]
    sum_abundants = sum(set(i + j for i, j in combinations_with_replacement(abundant_numbers, 2) if i + j < upper_limit))
    sum_all_numbers = upper_limit * (upper_limit - 1) // 2
    return sum_all_numbers - sum_abundants


if __name__ == '__main__':
    print(main())
    # 4179871 in 2.77sec
