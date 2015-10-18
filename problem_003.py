# coding: utf-8

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


from helpers import prime_powers


def result(number):
    return max([_tuple[0] for _tuple in prime_powers(number)])


def test_result():
    assert result(9) == 3


def main():
    result(600851475143)


if __name__ == '__main__':
    test_result()
    print(main())
    # 6857 in 376 usec
