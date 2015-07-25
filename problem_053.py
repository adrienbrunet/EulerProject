# coding: utf-8

# For 1 < n < 100, cb de k parmi sont > 10 ** 6

from math import factorial


def result():
    count = 0
    for n in range(1, 100):
        for k in range(1, n // 2 + 1):
            if factorial(n) / (factorial(n - k) * factorial(k)) > 1000000:
                count += 1
    return count


if __name__ == '__main__':
    print(result())
    # 2010
