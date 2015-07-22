# coding: utf-8

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

# PRO TIPS: checks if % 3 == 0
# 1 + ... + 9 = 45 --> % 3 == 0
# 1 + ... + 8 = 36 --> % 3 == 0
# 1 + ... + 7 = 28
# 1 + ... + 6 = 21 --> % 3 == 0
# 1 + ... + 5 = 15 --> % 3 == 0
# 1 + ... + 4 = 10
# 1 + 2 + 3   = 6  --> % 3 == 0
# 1 + 2       = 3  --> % 3 == 0

# We only need to look for number with 7 digits
# otherwise pandigits are divisible by 3 and thus not prime (or smaller)


from helpers import eratosthene


def is_ndigital(number, n=9):
    if len(set(str(number))) != 7:
        return False
    return ''.join(sorted(str(number))) == ''.join([str(i) for i in range(1, n+1)])


def result():
    _max = 0
    for i in eratosthene(7654321):
        if i < 10 ** 6:
            continue
        else:
            if is_ndigital(i, 7) and i > _max:
                _max = i
    return _max


if __name__ == '__main__':
    print(result())
    # 7652413
