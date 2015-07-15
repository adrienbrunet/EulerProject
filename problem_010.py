# coding: utf-8


'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


''' Ran in 22 sec... Should be optimized...'''


from helpers import eratosthene


def result(_max):
    return sum(eratosthene(_max))


def test_result():
    assert result(10) == 17


if __name__ == '__main__':
    test_result()
    print(result(2000000))
    # 142913828922
