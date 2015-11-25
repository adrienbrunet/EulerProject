# coding: utf-8


'''
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''


def get_index_for_fibonacci_with_digit(_max):
    _list = [1, 1]
    while len(str(_list[-1] + _list[-2])) < _max:
        _list.append(_list[-1] + _list[-2])
    return len(_list) + 1


def test_get_index_for_fibonacci_with_digit():
    assert get_index_for_fibonacci_with_digit(2) == 7


def main():
    return get_index_for_fibonacci_with_digit(1000)

if __name__ == '__main__':
    test_get_index_for_fibonacci_with_digit()
    print(main())
    # 4782 in 37.1ms
