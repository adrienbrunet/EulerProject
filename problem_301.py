'''
Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as follows:
- At the start of the game there are three heaps of stones.
- On his turn the player removes any positive number of stones from any single heap.
- The first player unable to move (because no stones remain) loses.

If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and n3 then there is a simple function X(n1,n2,n3) — that you may look up or attempt to deduce for yourself — that returns:

zero if, with perfect strategy, the player about to move will eventually lose; or
non-zero if, with perfect strategy, the player about to move will eventually win.
For example X(1,2,3) = 0 because, no matter what the current player does, his opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by his opponent until no stones remain; so the current player loses. To illustrate:
- current player moves to (1,2,1)
- opponent moves to (1,0,1)
- current player moves to (0,0,1)
- opponent moves to (0,0,0), and so wins.

For how many positive integers n ≤ 2 ** 30 does X(n,2n,3n) = 0 ?
'''


'''
From wikipedia: https://en.wikipedia.org/wiki/Nim#Mathematical_theory
XOR !!!
It's also fibonacci(30 + 2)
Facts:
   3n = 2n + n.
   a ^ b = 0 iff a = b. (from digital logic)
   a + b = (a ^ b) + ((a & b) << 1). (from digital logic)
Hence:
   n ^ 2n ^ 3n = 0                          (what we want)
   iff n ^ 2n = 3n                          (from the second fact)
   iff n ^ 2n = (n ^ 2n) + ((n & 2n) << 1)  (from the third fact)
   iff (n & 2n) << 1 = 0                    (by cancelling on both sides)
   iff n & 2n = 0                           (left-shifting doesn't change zeroness)
   iff the binary representation of n does not have consecutive '1' bits.

How many binary strings of length i have no consecutive 1's?
   First partition the set into strings that begin with a 0 and strings that begin with a 1.
   For those that begin with a 0, the rest of the string can be any string of length i-1 that doesn't have consecutive 1's.
   For those that begin with a 1, the rest of the string can be any string of length i-1 that begins with a 0 and doesn't have consecutive 1's.
Let numStrings(i, j) be the number of bit strings of length i that begin with the bit j and have no consecutive 1's. Then:
   numStrings(1, 0) = 1.  (base case)
   numStrings(1, 1) = 1.  (base case)
   numStrings(i, 0) = numStrings(i-1, 0) + numStrings(i-1, 1).  (for i >= 2)
   numStrings(i, 1) = numStrings(i-1, 0).                       (for i >= 2)
This corresponds to a shifted Fibonacci sequence, because:
   numStrings(i, 0) = numStrings(i-1, 0) + numStrings(i-2, 0).  (substitute)
   numStrings(1, 0) = 1.  (base case)
   numStrings(2, 0) = 2.  (derived)
   So numStrings(i, 0) = fibonacci(i + 1).
What we want is numStrings(30, 0) + numStrings(30, 1) = numStrings(31, 0) = fibonacci(32).
'''


def slow_main():
    _sum = 0
    for n in range(1, 2 ** 30 + 1):
        if n ^ (2 * n) ^ (3 * n) == 0:
            _sum += 1
    return _sum


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    return fibonacci(30 + 2)
    #  13.5 usec per loop


if __name__ == '__main__':
    print(main())
