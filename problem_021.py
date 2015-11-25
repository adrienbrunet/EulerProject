# coding: utf-8

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


from helpers import factors


def create_amicable_list():
    return {i: sum(list(factors(i)[:-1])) for i in range(2, 10001)}


_list = create_amicable_list()


def test_create_amicable_list():
    assert _list[220] == 284
    assert _list[284] == 220


def main():
    to_sum = []
    for el in _list:
        key = _list[el]
        if key in _list and _list[key] == el and key != el:
            to_sum.append(el)

    return sum(to_sum)


if __name__ == '__main__':
    test_create_amicable_list()
    print(main())
    # 31626 in 1.75ms
