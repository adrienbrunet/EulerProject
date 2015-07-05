# coding: utf-8

'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''


from math import sqrt


def list_factor(number):
    ''' Give the list of factor of a given number'''
    return set([j for i in range(1, int(sqrt(number)) + 1) for j in [i, number // i] if number % i == 0])


def test_list_factor():
    assert list_factor(20) == {1, 20, 2, 10, 4, 5}


def result(nb_divisor):
    list_triangle_numbers = [sum(range(i + 1)) for i in range(10000, 20000)]
    for el in list_triangle_numbers:
        if len(list_factor(el)) > 500:
            print el
            break


test_list_factor()

result(1)
