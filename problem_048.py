# coding: utf-8

'''
The series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 10 ** 10 = 10405071317.

Find the last ten digits of the series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 1000 ** 1000.
'''


def result(_max):
    return str(sum([i ** i for i in range(1, _max + 1)]))[-10:]


def test_result():
    assert result(10) == '0405071317'


def main():
    return result(1000)


if __name__ == '__main__':
    test_result()
    print(main())
    # 9110846700 in 11ms
