# coding: utf-8

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''


from itertools import combinations_with_replacement, permutations
from math import factorial


def result_naive():
    _list = []
    for i in range(10, 10000000):
        if '9' in str(i) and i < 362880:
            continue
        if sum([factorial(int(nb)) for nb in str(i)]) == i:
            _list.append(i)
    return _list


def result():
    _list = []
    for i in range(2, 7):
        list_combinaisons = combinations_with_replacement('0123456789', i)
        for combinaison in list_combinaisons:
            sum_factorial = sum(map(factorial, (map(int, combinaison))))
            if len(str(sum_factorial)) == len(combinaison):
                if(combinaison in permutations(str(sum_factorial), i)):
                    list.append(sum_factorial)
    return sum(_list)


if __name__ == '__main__':
    print(result())
    # 40730
