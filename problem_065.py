# coding: utf-8


'''
    The square root of 2 can be written as an infinite continued fraction.
    sqrt(2) = 1 + 1 / (2 +  1 / ( 2 + 1 / ( 2 + 1 / ( 2  + ...))))  

    The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

    It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.
    3/2
    7/5
    17/12
    41/29

    Hence the sequence of the first ten convergents for √2 are:
    1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, …

    What is most surprising is that the important mathematical constant,
    e = [2; 1,2,1, 1,4,1, 1,6,1 , … , 1,2k,1, …].

    The first ten terms in the sequence of convergents for e are:
    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, …

    The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

    Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

# from http://math.arizona.edu/~thakur/cf2.pdf,
# I get the following formulae for the denominator:
# n_k = a_k\cdot n_{k-1} + n_{k-2}


def result(_max):
    nk, nk1 = 2, 3
    for nb in range(3, _max + 2):
        if not nb % 3:
            ak = 2 * (nb // 3)
        else:
            ak = 1
        nk, nk1 = nk1, ak * nk1 + nk
    return sum(int(digit) for digit in str(nk))


def main():
    return result(100)

if __name__ == '__main__':
    assert result(10) == 17
    print(main())
    # 272 in 38.9 usec
