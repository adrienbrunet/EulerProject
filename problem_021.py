# coding: utf-8

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


from math import sqrt


def list_factor(number):
    ''' Give the list of factor of a given number'''
    _result = set([j for i in range(1, int(sqrt(number)) + 1) for j in [i, number // i] if number % i == 0])
    _result.remove(max(_result))
    return _result


def test_list_factor():
    assert list_factor(20) == {1, 2, 10, 4, 5}


test_list_factor()


_list = {i: sum(list(list_factor(i))) for i in range(2, 10001)}

assert _list[220] == 284
assert _list[284] == 220

to_sum = []
for el in _list:
    key = _list[el]
    if key in _list and _list[key] == el and key != el:
        to_sum.append(el)

print sum(to_sum)
