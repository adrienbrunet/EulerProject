# coding: utf-8

'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand        Player 1        Player 2        Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD  Player 2
        Pair of Fives       Pair of Eights

2       5D 8C 9S JS AC      2C 5C 7D 8S QH  Player 1
        Highest card Ace    Highest card Queen

3       2D 9C AS AH AC      3D 6D 7D TD QD  Player 2
        Three Aces          Flush with Diamonds


4       4D 6S 9H QH QC      3D 6D 7H QD QS  Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D  Player 1
        Full House          Full House
        With Three Fours    with Three Threes


The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''


from collections import namedtuple, Counter
import csv


card = namedtuple('Card', ['value', 'color'])


class PokerHand(object):
    ranking = '23456789TJQKA'
    mapping = {key: counter for counter, key in enumerate(ranking, start=2)}

    rules = [
        (1, 1, 1, 1, 1),  # High Card: Highest value card.
        (2, 1, 1, 1),  # One Pair: Two cards of the same value.
        (2, 2, 1),  # Two Pairs: Two different pairs.
        (3, 1, 1),  # Three of a Kind: Three cards of the same value.
        'Straight',  # Straight: All cards are consecutive values.
        'Flush',  # Flush: All cards of the same suit.
        (3, 2),  # Full House: Three of a kind and a pair.
        (4, 1),  # Four of a Kind: Four cards of the same value.
        'Straigt Flush',  # Straight Flush: All cards are consecutive values of same suit.
        'Royal Flush',  # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    ]
    # Straight, and Flushes are corner case of (1, 1, 1, 1, 1),
    # we can just check for them and then apply rule of highest value

    def __init__(self, hand):
        self.hand = [card(value=c[0], color=c[1]) for c in hand]
        self.hand_value = list(zip(
            *sorted(
                ((v, self.mapping[k]) for (k, v) in Counter(card.value for card in self.hand).items()),
                reverse=True)))
        if self.hand_value[0] == (1, 1, 1, 1, 1):
            if self.is_straight():
                if self.is_flush():
                    self.hand_value[0] = 'Straight Flush'
                else:
                    self.hand_value[0] = 'Straight'
            if self.is_flush():
                if self.hand_value[1][0] == 14:
                    self.hand_value[0] = 'Royal Flush'
                else:
                    self.hand_value[0] = 'Flush'

    def is_straight(self):
        if self.hand_value[0] != (1, 1, 1, 1, 1):
            return False
        if ''.join(str(_) for _ in sorted(self.hand_value[1])) in self.ranking * 2:
            return True

    def is_flush(self):
        return len(set(card.color for card in self.hand)) == 1

    def __lt__(self, other):
        if self.rules.index(self.hand_value[0]) > self.rules.index(other.hand_value[0]):
            return False
        if self.rules.index(self.hand_value[0]) == self.rules.index(other.hand_value[0]):

            for i in range(5):
                if self.hand_value[1][i] > other.hand_value[1][i]:
                    return False
                if self.hand_value[1][i] < other.hand_value[1][i]:
                    return True
        if self.rules.index(self.hand_value[0]) < self.rules.index(other.hand_value[0]):
            return True


def main():
    result = 0
    for line in csv.reader(open('./problem_054.input.txt'), delimiter=' '):
        hand1, hand2 = PokerHand(line[0:5]), PokerHand(line[5:])
        if hand1 > hand2:
            result += 1
    return result


if __name__ == '__main__':
    assert not PokerHand(['5H', '5C', '6S', '7S', 'KD']) > PokerHand(['2C', '3S', '8S', '8D', 'TD'])
    assert PokerHand(['5D', '8C', '9S', 'JS', 'AC']) > PokerHand(['2C', '5C', '7D', '8S', 'QH'])
    assert not PokerHand(['2D', '9C', 'AS', 'AH', 'AC']) > PokerHand(['3D', '6D', '7D', 'TD', 'QD'])
    assert PokerHand(['4D', '6S', '9H', 'QH', 'QC']) > PokerHand(['3D', '6D', '7H', 'QD', 'QS'])
    assert PokerHand(['2H', '2D', '4C', '4D', '4S']) > PokerHand(['3C', '3D', '3S', '9S', '9D'])
    print(main())
    # 376 in 66.8ms
