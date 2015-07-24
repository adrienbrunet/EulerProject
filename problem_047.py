# coding: utf-8


'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''


from helpers import prime_powers


def result():
    _list_consecutive = []
    for number in range(2 * 3 * 5 * 7, 10 ** 6):
        if len(_list_consecutive) == 4:
            return _list_consecutive[0]

        if len(list(prime_powers(number))) == 4:
            _list_consecutive.append(number)
        else:
            _list_consecutive = []


if __name__ == '__main__':
    print(result())
    # 134043
