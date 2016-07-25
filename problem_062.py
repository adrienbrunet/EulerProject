# -*- coding: utf-8 -*-

'''
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''


def main():
    cubes = [str(n ** 3) for n in range(int(1e5))]
    perms = {}
    for cube in cubes:
        key_from_digits = ''.join(sorted(cube))
        perms[key_from_digits] = perms.get(key_from_digits, []) + [cube]
    return min([min(map(int, cube_list)) for key, cube_list in list(perms.items()) if len(cube_list) == 5])


if __name__ == '__main__':
    print(main())  # 343 msec
