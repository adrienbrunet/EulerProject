# coding: utf-8


'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''


# Hint by @jollivier: number is 6-digit (now, it's like I've cheated, thanks)

# Last digits can't be replace (it wouldn't be a prime anymore with the replacements)
# 5 replaced digits --> Not possible. (we can generate thm and check if they're prime)
# We can reduce th problem to look for the number with 3 '0', '1', '2'
# and generate the mask from here 'cause we're looking for the smaller number
# I began to search for all permutations of mask with 2 and 4 digits which are replaced.
# BUT (#genius), if we have 2 or 4 replacement, it won't be possible to be a prime. WHY?
# Because of fancy ass rule "number % 3 != 0 ==> sum_digits % 3 != 0"
# \o/ CAPS LOCK MATH IS BEST MATH \o/


from helpers import eratosthene, is_prime


def get_digit_count_dict(number):
    list_digits = str(number)
    return {digit: list_digits.count(digit) for digit in '0123456789'}


def main():
    list_primes = list(eratosthene(1000000))

    for prime in list_primes:
        if prime < 100000:
            continue

        dict_count = get_digit_count_dict(prime)
        for _str in ['0', '1', '2']:
            if dict_count[_str] >= 3:
                size = 0
                error = 0
                # replace all numbers
                mask = str(prime).replace(_str, '.')
                for other_digit in range(int(_str), 10):
                    if error > 3:
                        break
                    if is_prime(int(mask.replace('.', str(other_digit)))):
                        size += 1
                    else:
                        error += 1
                if size == 8:
                    return prime


if __name__ == '__main__':
    print(main())
    # 121313 in 57.7ms
