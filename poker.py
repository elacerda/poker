#!/usr/bin/python
"""
 By Eduardo A. D. Lacerda
 Simple poker round to analyze hand statistics.
"""
import sys
import random
import itertools

class poker(object):
    def __init__(self):
        self._create_cards()
        self.shuffle()
    def _create_cards(self):
        _SUITS = 'cdhs'
        _RANKS = '23456789TJQKA'
        self._deck = tuple(''.join(card) for card in itertools.product(_RANKS, _SUITS))

    def shuffle(self):
        random.seed()
        return random.sample(self._deck, 52)

    def hand(self, players, deck):
        print 'Hand for %d players' % players
        hands = []
        for p_i in range(players):
            print '\nPlayer: %d' % (p_i+1)
            hand = [deck.pop() for n in range(2)]
            print hand
            hands.append(hand)
        return hands, deck
    
    def flop(self, deck):
        print '\nFLOP\n'
        flop = [deck.pop() for n in range(3)]
        print flop
        return flop, deck

    def turn(self, deck):
        print '\nTURN\n'
        turn = deck.pop()
        print turn
        return turn, deck

    def river(self, deck):
        print '\nRIVER\n'
        river = deck.pop()
        print river
        return river, deck

    def round(self, players=9):
        deck = self.shuffle()
        players_hand, deck = self.hand(players, deck)
        flop, deck = self.flop(deck)
        turn, deck = self.turn(deck)
        river, deck = self.river(deck)


def codds(odds, call, pote):
    pote_final = pote + call
    ratio = 1. * call/pote_final
    odds_ratio = 0.01 * (odds * 4. + 2.)
    if odds_ratio > ratio: 
        print 'CALL!'
    else:
        print 'FOLD!'

def main(argv):
    try:
        players = int(argv[1])
    except IndexError:
        players = 2
    P = poker()
    P.round(players=players)

if __name__ == '__main__':
    main(sys.argv)
