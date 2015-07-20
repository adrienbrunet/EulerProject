# coding: utf-8


from itertools import chain, cycle, accumulate  # accumuate, python3 only
from math import sqrt


def memoize(f):
    """ Memoization decorator for a function taking a single argument """
    class MemoDict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return MemoDict().__getitem__


def memoize_multiple_args(f):
    """ Memoization decorator for a function taking many arguments """
    class MemoDict(dict):
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return MemoDict(f)


def is_power(a, b):
    ''' Check if a is a power of b'''
    return True if isinstance(a, int) and isinstance(b, int) and (a > 0 and b > 0) and (a == b or (b != 1 and not a % b and is_power(a // b, b))) else False


def prime_powers(number):
    '''
    Find the prime powers of a number.
    It returns a tuple of tuple with power of prime in each
    '''

    # almost_prime goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
    for almost_prime in accumulate(chain([2, 1, 2], cycle([2, 4]))):
        if almost_prime ** 2 > number:
            break
        # If almost_prime is a prime power, it will be catch in prime_powers
        # otherwise we'll get the continue because number % almost_prime
        if number % almost_prime:
            continue

        prime_powers, prime = (), almost_prime
        while not number % almost_prime:
            number = number // almost_prime
            prime_powers += (prime, )
            prime *= almost_prime
        yield(prime_powers)
    if number > 1:
        yield((number, ))


@memoize
def factors(number):
    factors = [1]
    for _prime in prime_powers(number):
        factors += [factor * prime for factor in factors for prime in _prime]
        factors.sort()
    return factors


@memoize
def is_prime(number):
    if number < 2:
        return False
    for divisor in accumulate(chain([2, 1, 2], cycle([2, 4]))):
        if divisor ** 2 > number:
            break
        if not number % divisor:
            return False
    return True


def eratosthene(limit):
    """ using a 235 wheel. Inspired from rosettacode.org"""
    for _ in [2, 3, 5]:
        yield(_)
    if limit < 7:
        return
    mod_prime = [7, 11, 13, 17, 19, 23, 29, 31]
    gaps = [4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 4, 6, 2, 6]
    indexes = [0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7]
    limit_bf = (limit + 23) // 30 * 8 - 1
    limit_sqrt = (int(sqrt(limit)) - 7)
    buf = [True] * (limit_bf + 1)
    for i in range(limit_sqrt + 1):
        if buf[i]:
            ci = i & 7
            p = 30 * (i >> 3) + mod_prime[ci]
            s = (p ** 2) - 7
            p8 = p << 3
            for j in range(8):
                c = s // 30 * 8 + indexes[s % 30]
                buf[c::p8] = [False] * ((limit_bf - c) // p8 + 1)
                s += p * gaps[ci]
                ci += 1
    for i in range(limit_bf - 6 + (indexes[(limit - 7) % 30])):
        if buf[i]:
            yield((30 * (i >> 3) + mod_prime[i & 7]))


def eratosthene_slow(limit):
    non_primes = [False] * (limit + 1)
    primes = []

    for i in range(2, limit):
        if non_primes[i]:
            continue
        for multiple in range(i ** 2, limit, i):
            non_primes[multiple] = True

        primes.append(i)

    return primes


def test_prime_powers():
    """ for testing purpose we evaluate as a list the generator"""
    assert list(prime_powers(3)) == [(3,)]
    assert list(prime_powers(10000)) == [(2, 4, 8, 16), (5, 25, 125, 625)]


def test_factors():
    assert factors(6) == [1, 2, 3, 6]
    assert factors(3) == [1, 3]


def test_is_prime():
    assert is_prime(3)
    assert is_prime(23)
    assert not is_prime(25)
    assert not is_prime(8672849567249646)


def test_is_power():
    assert is_power(4096, 2)
    assert is_power(3 ** 130, 3)
    assert not is_power(10, 5)


def test_eratosthene():
    assert eratosthene(20) == [2, 3, 5, 7, 11, 13, 17, 19]


if __name__ == '__main__':
    test_prime_powers()
    test_factors()
    test_is_prime()
    test_is_power()
