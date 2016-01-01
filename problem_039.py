# coding: utf-8

'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

# Analysis: a <= b < c => a < p/3

# a^2 + b^2 = c^2
# a + b + c = p

# ==> c = p  – a – b
#     a^2 + b^2 = (p - a - b)^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab ==> p^2 + 2pa + 2ab - 2pb = 0

# ==> b can be written: p(p - 2a) / 2(p - a)


def main():
    perimeter = 0
    max_solution = 0

    for p in range(2, 1001):
        nb_solution = 0
        for a in range(2, p // 3):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                nb_solution += 1
        if nb_solution > max_solution:
            max_solution = nb_solution
            perimeter = p
    return perimeter


if __name__ == '__main__':
    print(main())
    # 840 in 40.7ms
