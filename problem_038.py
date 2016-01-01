# coding: utf-8


'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def is_9pandigital(number):
    return ''.join(sorted(str(number))) == '123456789'


def test_is_9pandigital():
    assert is_9pandigital(987654321)
    assert not is_9pandigital(9976654321)


def main():
    '''
    We look for the largest number.
    The example gives 9 and (1, 2, 3, 4, 5) -->  918273645 and it's not the solution
    As it's a 9pandigital, it will then start with a 9!

    We can see that if x >= 5, 9x__ * 2 = 19___, x must be < 5
    We consider the product with n \ 9213 < n < 9487 with (1, 2)

    We consider the product with 9x with 2 < x < 8
    We have 92 93 94 as candidates
    But the concatenation of the products with 1, 2, 3, 4 gives more than 9 digits

    We consider the product withn \ 921 < n < 987
    But the concatenation of the products with 1, 2, 3 gives more than 9 digits

    We need to consider product with n \ 9213 < n < 9487

    Above 4digits numbers, we exceed 9 digits in the concatenation
    and the multiplier tuple is as least (1, 2)
    '''
    for number in range(9487, 9213, -1):
        concatenation = str(number) + str(number * 2)
        if is_9pandigital(concatenation):
            return concatenation


if __name__ == '__main__':
    test_is_9pandigital()
    print(main())
    # 932718654 in 326 µs
