# coding: utf-8

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''


import itertools


def make_int(n):
    return int(''.join(map(str, n)))


def is_9pandigital(permutation, product):
    """Check we have only once each digit from 1 to 9"""
    return ''.join(sorted("".join(map(str, permutation)) + str(product))) == "123456789"


def product_half_splitted_at(permutation, n):
    return make_int(permutation[:n]) * make_int(permutation[n:])


def main():
    products = set()
    target = range(1, 10)
    for permutation in itertools.permutations(target, 5):
        if permutation[4] == 5:  # 5 * x ends with 5 or 0...
            continue
        for len_multiplicand in [1, 2]:  # product x * xxxx and xx * xxx
            if permutation[len_multiplicand - 1] != 5:
                product = product_half_splitted_at(permutation, len_multiplicand)
                if is_9pandigital(permutation, product):
                    products.add(product)
    return sum(list(products))


if __name__ == '__main__':
    print(main())
    # 45228 in 155ms
