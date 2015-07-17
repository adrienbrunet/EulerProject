# coding: utf-8

'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''


def result(money):
    coin_values = [1, 2, 5, 10, 20, 50, 100, 200]  # in cents
    memo_nb_possibilities_to_make = {i: 0 for i in range(money + 1)}  # init with 0
    memo_nb_possibilities_to_make[0] = 1  # 0 * 1 + 0 * 2 + ...
    for value in coin_values:
        for target in range(value, money + 1):
            memo_nb_possibilities_to_make[target] += memo_nb_possibilities_to_make[target - value]
    return memo_nb_possibilities_to_make[money]


if __name__ == '__main__':
    print(result(200))
    # 73682
