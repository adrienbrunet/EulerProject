# coding: utf-8

'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''


def permute(s):
    return [s] if len(s) == 1 else [c + perm for i, c in enumerate(s) for perm in permute(s[:i] + s[i + 1:])]


def test_permute():
    assert permute('a') == ['a']
    assert permute('ab') == ['ab', 'ba']


test_permute()


_list = permute('1234567890')
_list.sort()
print _list[999999]
