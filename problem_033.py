# coding: utf-8

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import fractions


def main():
    p = fractions.Fraction(1, 1)
    for numerator in range(10, 100, 1):
        for denominator in range(numerator + 1, 100, 1):
            # trivial examples
            if not denominator % 10 or numerator == denominator:
                continue
            # Decompose: x * 10 + a / a < 10
            prod_num, prod_den = [numerator // 10, numerator % 10], [denominator // 10, denominator % 10]
            # search common factor
            if any(i in prod_den for i in prod_num) and any(i not in prod_den for i in prod_num):
                common = prod_num[0] if prod_num[0] in prod_den else prod_num[1]
                prod_num.remove(common)
                prod_den.remove(common)
                simple_num, simple_den = prod_num[0], prod_den[0]
                if numerator * simple_den == denominator * simple_num:
                    p *= fractions.Fraction(simple_num, simple_den)
    return p


if __name__ == '__main__':
    print(main())
    # 1/100 in 5.54ms
