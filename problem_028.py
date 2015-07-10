# coding: utf-8

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''


def trinome(n):
    return 4 * (n ** 2) - (6 * (n - 1))


def diag(n):
    return 1 + sum([trinome(i) for i in range(3, n + 1, 2)])


print trinome(3)
print trinome(5)
print '-' * 80
print diag(1)
print diag(3)
print diag(5)
print diag(1001)
