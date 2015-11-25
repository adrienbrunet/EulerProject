# coding: utf-8

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''


def recurring_cycle_length(number):
    decimals = []

    remainder = 1
    while remainder:
        remainder = remainder % number
        if remainder in decimals:
            return len(decimals) - decimals.index(remainder)
        decimals.append(remainder)
        remainder *= 10
    return 0


def test_recurring_cycle():
    assert recurring_cycle_length(2) == 0
    assert recurring_cycle_length(3) == 1
    assert recurring_cycle_length(7) == 6
    assert recurring_cycle_length(10) == 0


test_recurring_cycle()


def main():
    _list = [recurring_cycle_length(n) for n in range(1, 1000)]
    return _list.index(max(_list)) + 1  # index starts at 0


if __name__ == '__main__':
    print(main())
    # 983 in 300ms
