# coding: utf-8

'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''


from itertools import accumulate

from helpers import eratosthene


def result(_max):
    list_primes = list(eratosthene(_max))
    list_sum = list(accumulate(list_primes))

    length = 0
    for counter, i in enumerate(list_sum):
        if i in list_primes and counter > length:
            length = counter
            result = i

    for i in range(len(list_sum)):
        for j in range(i - length - 1, 0, -1):
            diff = list_sum[i] - list_sum[j]
            if diff > _max:
                break
            if diff in list_primes:
                length = i - j
                result = diff

    return result


def test_result():
    assert result(100) == 41
    assert result(1000) == 953


if __name__ == '__main__':
    test_result()
    print(result(1000000))
