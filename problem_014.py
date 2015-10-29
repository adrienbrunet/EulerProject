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


class Collatz(object):
    memo = {1: 1}

    def collatz_suite(self, number, iteration=0):
        iteration += 1
        if number in self.memo:
            return self.memo[number]
        else:
            if number % 2:
                self.memo[number] = self.collatz_suite(3 * number + 1)
            else:
                self.memo[number] = self.collatz_suite(number >> 1)
            return self.memo[number] + iteration


def test_collatz_suite():
    solver = Collatz()
    response = solver.collatz_suite(13)
    assert response == 10


def main():
    solver = Collatz()
    _max = 1
    for i in range(1, 1000000, 2):
        collatz = solver.collatz_suite(i)
        if collatz > _max:
            _max = collatz
            rep = i
    return rep


if __name__ == '__main__':
    test_collatz_suite()
    print(main())
    # 837799 in 288ms
