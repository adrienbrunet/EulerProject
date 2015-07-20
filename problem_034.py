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
    facts = [(factorial(i), str(i)) for i in range(10)]
    for nb_perm in range(1, 6 + 1):
        for _tuple in combinations_with_replacement(facts, nb_perm):
            _sum = sum([t[0] for t in _tuple])
            base_nb = "".join([t[1] for t in _tuple])

            for perm in permutations(base_nb):
                str_perm = "".join(perm)
                if str_perm.startswith('0'):
                    continue
                number = int(str_perm)
                if number == _sum:
                    if number > 10:
                        _list.append(number)
                    break
    return sum(set(_list))


if __name__ == '__main__':
    print(result())
    # 40730
