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
        self.ncards = 52
        self.ncards_players = 2
        self.ncards_flop = 3

    def _create_cards(self):
        _SUITS = 'cdhs'
        _RANKS = '23456789TJQKA'
        self._deck = tuple(''.join(card) for card in itertools.product(_RANKS, _SUITS))

    def shuffle(self):
        random.seed()
        return random.sample(self._deck, self.ncards)

    def hand(self, players, deck):
        print 'Hand for %d players' % players
        hands = []
        for p_i in range(players):
            print '\nPlayer: %d' % (p_i+1)
            hand = [deck.pop() for n in range(self.ncards_players)]
            print hand
            hands.append(hand)
        return hands, deck

    def flop(self, deck):
        print '\nFLOP\n'
        flop = [deck.pop() for n in range(self.ncards_flop)]
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

    def round_example(self, players=9):
        deck = self.shuffle()
        hands, deck = self.hand(players, deck)
        flop, deck = self.flop(deck)
        turn, deck = self.turn(deck)
        river, deck = self.river(deck)
        '''
            Here do stuff with:
            HANDS, FLOP, TURN, RIVER and the rest of the DECK
            Ex: create a winner decision method:
            self.winner_hand(hands, flop, turn, river)
        '''


class player(object):
    '''
        Starting to create an usable player class to play poker.
    '''
    def __init__(self, name='noname', chips=10000):
        self._name = name
        self._chips = chips
        self._hand = None

    def set_hand(self, hand):
        self._hand = hand

    def get_hand(self):
        return self._hand

    def get_chips(self):
        return self._chips


def codds(odds, call, pot):
    '''
        should I call or fold by odds ?
    '''
    final_pot = pot + call
    ratio = 1. * call/final_pot
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
