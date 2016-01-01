# coding: utf-8

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from itertools import permutations


from helpers import eratosthene


def main():
    list_primes = list([i for i in eratosthene(9999) if i > 1489])

    for counter, prime in enumerate(list_primes):
        for second_prime in list_primes[counter + 1:]:
            # We need four equidistant primes. It should stay below 10000
            third_prime = second_prime + (second_prime - prime)
            if third_prime > 9999:
                break
            if third_prime in list_primes:
                # Check there are permutations
                perms = list(permutations(str(prime)))
                if tuple(str(third_prime)) in perms and tuple(str(second_prime)) in perms:
                    return str(prime) + str(second_prime) + str(third_prime)


if __name__ == '__main__':
    print(main())
    # 296962999629 in 1.29sec
