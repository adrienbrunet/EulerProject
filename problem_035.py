# coding: utf-8

'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from helpers import eratosthene


def result(_max):
    total = 0
    even_numbers = set('024568')
    list_primes_under_max = [i for i in eratosthene(_max)]
    for i in list_primes_under_max:
        str_i = str(i)
        if not even_numbers.is_disjoint(str_i):
            continue
        permutations = {int(str_i[j:] + str_i[:j]) for j in range(len(str_i))}
        if all(perm >= i and perm in list_primes_under_max for perm in permutations):
            total += len(permutations)
    return 2 + total  # we skipped 2 and 5


def test_result():
    assert result(100) == 13


def main():
    return result(1000000)

if __name__ == '__main__':
    test_result()
    print(main())
    # 55 in 1.02sec
