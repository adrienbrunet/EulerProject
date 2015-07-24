# coding: utf-8

'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2×1**2
    15 = 7 + 2×2**2
    21 = 3 + 2×3**2
    25 = 7 + 2×3**2
    27 = 19 + 2×2**2
    33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''


from helpers import is_prime


def result():
    list_2squares = [2 * (n ** 2) for n in range(1, 708)]  # 708 > sqtr(500 000)

    for number in range(3, 10 ** 6, 2):
        if not is_prime(number) and all([not is_prime(number - _2square) for _2square in list_2squares if _2square < number]):
            return number


if __name__ == '__main__':
    print(result())
    # 5777
