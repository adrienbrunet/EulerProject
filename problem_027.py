# coding: utf-8

'''
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''


from helpers import is_prime


def binome(a, b):
    def f(n):
        return n ** 2 + a * n + b
    return f


def result(n):
    _max = 1
    _max_a = 1
    _max_b = 1
    first_primes = [j for j in range(n + 1) if is_prime(j)]
    for a in range(- n, n + 1):
        for b in first_primes:
            i = 0
            while is_prime(binome(a, b)(i)):
                i += 1
            if i >= _max:
                _max = i
                _max_a = a
                _max_b = b

    return _max_a * _max_b


if __name__ == "__main__":
    print(result(1000))
