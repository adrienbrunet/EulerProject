# -*- coding: utf-8 -*-

'''
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''


def main():
    # - why 25? It's a bit random, I tried with 100, 50, 30, 25, 20.
    # I had the same results until 20.
    # - why 50? tried with 100 first, then saw that nbs gets quickly high
    # with the powers so it's not worth the computations
    # *** Performance is a bit better narrowing the scope of the lists
    # but it's more empiric stuff than a clever tricK
    return sum(1 for number in range(1, 50) for n in range(1, 25) if len(str(number ** n)) == n)


if __name__ == '__main__':
    print(main())  # 49 in 651 usec
