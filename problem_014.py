# coding: utf-8

'''


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def memoize(f):
    memo = {1: 1}

    def helper(x, iteration=0):
        if x not in memo:
            memo[x] = f(x)
        return memo[x] + iteration

    return helper


@memoize
def collatz_suite(number, iteration=0):
    if number == 1:
        return iteration
    if number % 2:
        return collatz_suite(3 * number + 1, iteration + 1)
    else:
        return collatz_suite(number / 2, iteration + 1)


def test_collatz_suite():
    assert collatz_suite(13) == 10


def result():
    _max = 1
    rep = 1
    for i in range(1, 1000000):
        collatz = collatz_suite(i)
        if collatz > _max:
            _max = collatz
            rep = i
    return rep


test_collatz_suite()
print result()
