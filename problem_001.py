# coding: utf-8

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def multiple_from_list(_list):
    def multiple(number):
        for multiple in _list:
            if number % multiple == 0:
                return True
        return False
    return multiple


def sum_multiple_of_3_5_6_9_below(number):
    return sum(filter(multiple_from_list([3, 5, 6, 9]), range(number)))


def test_problem1():
    assert sum_multiple_of_3_5_6_9_below(10) == 23


if __name__ == '__main__':
    test_problem1()
    print(sum_multiple_of_3_5_6_9_below(1000))
    # 233168
