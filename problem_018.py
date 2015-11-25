# coding: utf-8


'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

L = [
    [int(i) for i in "75".split()],
    [int(i) for i in "95 64".split()],
    [int(i) for i in "17 47 82".split()],
    [int(i) for i in "18 35 87 10".split()],
    [int(i) for i in "20 04 82 47 65".split()],
    [int(i) for i in "19 01 23 75 03 34".split()],
    [int(i) for i in "88 02 77 73 07 63 67".split()],
    [int(i) for i in "99 65 04 28 06 16 70 92".split()],
    [int(i) for i in "41 41 26 56 83 40 80 70 33".split()],
    [int(i) for i in "41 48 72 33 47 32 37 16 94 29".split()],
    [int(i) for i in "53 71 44 65 25 43 91 52 97 51 14".split()],
    [int(i) for i in "70 11 33 28 77 73 17 78 39 68 17 57".split()],
    [int(i) for i in "91 71 52 38 17 14 91 43 58 50 27 29 48".split()],
    [int(i) for i in "63 66 04 68 89 53 67 30 73 16 69 87 40 31".split()],
    [int(i) for i in "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23".split()],
]

# For test purpose
L_test = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3],
]


def result(_list):
    for i in range(len(_list) - 1):
        line = _list[-(i + 1)]
        next_line = _list[-(i + 2)]
        for index in range(len(next_line)):
            left = line[index]
            right = line[index + 1]
            next_line[index] += max(left, right)

    return _list[0][0]


def test_result():
    assert result(L_test) == 23


def main():
    return result(L)


if __name__ == '__main__':
    test_result()
    print(result(L))
    # 1074 in 50.8usec
