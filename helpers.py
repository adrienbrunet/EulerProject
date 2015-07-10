# coding: utf-8


from itertools import chain, cycle, accumulate  # accumuate, python3 only


def memoize(f):
    """ Memoization decorator for a function taking a single argument """
    class MemoDict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return MemoDict().__getitem__


def memoize_multiple_args(f):
    """ Memoization decorator for a function taking a single argument """
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
    return factors


@memoize
def is_prime(number):
    if (not isinstance(number, int)) or number < 2:
        return False
    for divisor in accumulate(chain([2, 1, 2], cycle([2, 4]))):
        if divisor ** 2 > number:
            break
        if not number % divisor:
            return False
    return True


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


test_prime_powers()
test_factors()
test_is_prime()
test_is_power()
