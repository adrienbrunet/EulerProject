# coding: utf-8

'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import re


from helpers import is_prime


def is_truncatable_prime(n):
    for d in range(1, len(str(n))):
        if not is_prime(int(str(n)[d:])) or not is_prime(int(str(n)[:d])):
            return False
    return True


def test_is_truncatable_prime():
    assert not is_truncatable_prime(19)
    assert is_truncatable_prime(3797)


def main():
    # combinations of prime under 100 that are prime. 2, 3, 5 and 7 are skipped
    truncatable_primes = [23, 37, 53, 73]

    n = 101
    offset = 1

    while len(truncatable_primes) < 11:
        # alternative to use accumulate([2, 1, 2], cycle([2, 4]))
        n += 3 - offset  # 2 or 4
        offset *= -1

        # all truncatables number above 100 cannot contains even digits or 5
        if not re.search('[245680]', str(n)) and is_prime(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
    return sum(truncatable_primes)


if __name__ == '__main__':
    test_is_truncatable_prime()
    print(main())
    # 748317 in 345ms
