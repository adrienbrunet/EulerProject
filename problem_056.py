# coding: utf-8


'''
A googol (10 ** 100) is a massive number: one followed by one-hundred zeros; 100 ** 100 is almost unimginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''


def sum_digits(number):
    return sum([int(i) for i in str(number)])


def main():
    _max = 0
    for a in range(100):
        for b in range(100):
            if sum_digits(a ** b) > _max:
                _max = sum_digits(a ** b)
    return _max


if __name__ == '__main__':
    print(main())
    # 972 in 243ms
