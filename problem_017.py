# coding: utf-8

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.


If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

# EXTERNAL LIBRARY USED: inflect
import inflect
p = inflect.engine()


def count(number):
    word = p.number_to_words(number)
    word = word.replace(' ', '')
    word = word.replace('-', '')
    word = word.replace(',', '')
    return len(word)


def sum_count(_max):
    return sum([count(i) for i in range(1, _max + 1)])


def test_count():
    assert count(342) == 23
    assert count(115) == 20


def test_sum_count():
    assert sum_count(5) == 19


test_count()
test_sum_count()

print sum_count(1000)
