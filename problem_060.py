# -*- coding: utf-8 -*-

'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''


from helpers import eratosthene, fast_is_prime, memoize_multiple_args


class Node(object):
    '''
    This object will hold values for a tree with primes you can concatenate
    and still get new primes
    '''
    def __init__(self, value='0', parent=None, children=[]):
        self.value = value
        self.parent = parent
        self.children = children

        if self.parent is None:
            self.len_chain = 0
            self.sum = int(self.value)
        else:
            self.len_chain = self.parent.len_chain + 1
            self.sum = self.parent.sum + int(self.value)

    def __str__(self):
        if self.parent is None or self.parent.value == 0:
            return self.value
        else:
            return "%s, %s" % (self.parent, self.value)


@memoize_multiple_args
def concat_make_primes(prime1, prime2):
    if fast_is_prime(int(prime1 + prime2)) and fast_is_prime(int(prime2 + prime1)):
        return True
    return False


class Solver(object):
    list_tuple_result = []

    def add_grand_children(self, node):
        children = node.children

        for counter in range(len(children)):
            child1 = children[counter]
            child1.children = []
            for child2 in children[counter + 1:]:
                if concat_make_primes(child1.value, child2.value):
                    child1.children.append(Node(value=child2.value, parent=child1))
            if child1.len_chain < 5:
                if len(child1.children) >= 5 - child1.len_chain:
                    self.add_grand_children(child1)
            else:
                self.list_tuple_result.append(child1.sum)

    def solve(self, root):
        self.add_grand_children(root)
        return min(self.list_tuple_result)


def main():
    root = Node(value='0')
    root.children = [Node(value=str(p), parent=root) for p in eratosthene(10000)]
    return Solver().solve(root)


if __name__ == "__main__":
    print(main())
    # [13, 5197, 5701, 6733, 8389]
    # 26033
    # The slowest run took 37.89 times longer than the fastest. Result is cached in fast_is_prime
    # 1 loops, best of 3: 765 ms per loop
