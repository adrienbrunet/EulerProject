# coding: utf-8

'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''


def result():
    big_ass_string = ''.join(map(str, range(200000)))
    return int(big_ass_string[1]) * int(big_ass_string[10]) * int(big_ass_string[100]) * int(big_ass_string[1000]) * int(big_ass_string[10000]) * int(big_ass_string[100000]) * int(big_ass_string[1000000])


if __name__ == '__main__':
    print(result())
    # 210
