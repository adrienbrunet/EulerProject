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


def result(number):
    return sum(filter(multiple_from_list([3, 5, 6, 9]), range(number)))
    # This solution is a tiny bit slower but shorter
    # return sum(_ for _ in range(number) if not (number % multiple for multiple in [3, 5, 6, 9]))


def test_problem1():
    assert result(10) == 23


def main():
    result(1000)


if __name__ == '__main__':
    test_problem1()
    print(main())
    # 233168 in 613 usec
