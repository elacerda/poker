#!/usr/bin/python
"""
 By Eduardo A. D. Lacerda
 Simple poker round to analyze hand statistics.
"""
import sys
import random
import itertools


_suits = 'cdhs'
_ranks = '23456789TJQKA'


class Player(object):
    '''
        An usable player class to play poker.
    '''
    def __init__(self, name='noname', chips=10000):
        self.name = name
        self.pos = None
        self.chips = chips
        self.hand = None

    def purge_chips(self, nchips):
        self.chips -= nchips

    def add_chips(self, nchips):
        self.chips += nchips


class PokerTable(object):
    _deck = tuple(''.join(card) for card in itertools.product(_ranks, _suits))

    def __init__(self, deck=None):
        self.ncards = 52
        self.ncards_players = 2
        self.ncards_flop = 3
        self.hand_counter = 0
        self.players = []
        self.nplayers = 0

    def shuffle(self):
        random.seed()
        return random.sample(self._deck, self.ncards)

    def deal_players_hands(self, deck=None):
        if deck is None:
            deck = self.shuffle()
        # XXX TODO: 1 card per time
        for i, p in enumerate(self.players):
            hand = [deck.pop() for n in range(self.ncards_players)]
            p.hand = hand
        return deck

    def flop(self, deck):
        flop = [deck.pop() for n in range(self.ncards_flop)]
        return flop, deck

    def turn(self, deck):
        turn = [deck.pop()]
        return turn, deck

    def river(self, deck):
        river = [deck.pop()]
        return river, deck

    def add_player(self, name, chips, pos, player_instance=None):
        if player_instance is not None:
            p = player_instance
        else:
            p = Player(name, chips)
        p.pos = pos
        self.players.append(p)

    def _add_example_players(self, nplayers):
        for i in range(nplayers):
            name = 'Player %d' % (i+1)
            chips = 1500
            self.add_player(name=name, chips=chips, pos=i)
        self.nplayers = len(self.players)

    def remove_players(self):
        del self.players
        self.players = []
        self.nplayers = 0

    def round_example(self, nhands=10, nplayers=9):
        if nplayers > 10:
            nplayers = 10
        if self.nplayers == 0:
            self._add_example_players(nplayers)
        hand_counter = 0
        for n in range(nhands):
            print 'Poker hand #%d (table hand #%d)' % (hand_counter, self.hand_counter)
            print 'Hand for %d players' % self.nplayers
            deck = self.deal_players_hands()
            for i, p in enumerate(self.players):
                print '%s received: %s' % (p.name, p.hand)
            flop, deck = self.flop(deck)
            turn, deck = self.turn(deck)
            river, deck = self.river(deck)
            print 'Flop: %s' % flop
            print 'Turn: %s' % turn
            print 'River: %s' % river
            print '##########'
            print 'out deck - %d cards: %s' % (len(deck), deck)
            '''
                Here do stuff with:
                FLOP, TURN, RIVER and the rest of the DECK
                Ex: create a winner decision method:
                self.winner_after(flop, turn, river)
            '''
            hand_counter += 1
            self.hand_counter += 1
        self.remove_players()


def codds(outs, to_river=False):
    odds = outs * 2.
    if to_river:
        odds *= 2
    odds_frac = odds/100.
    return odds_frac/(1 - odds_frac)


def payornot(outs, pot, bet=None, to_river=False):
    card_odds = codds(outs, to_river)
    pot_odds = 1. * bet/(bet+pot)
    print 'Card ODDS: ', card_odds, ' - Pot ODDS: ', pot_odds
    if card_odds > pot_odds:
        print 'call or raise'
    else:
        print 'fold'


def main(argv):
    try:
        nhands = int(argv[1])
    except IndexError:
        nhands = 1
    try:
        nplayers = int(argv[2])
    except IndexError:
        nplayers = 2
    Table = PokerTable()
    Table.round_example(nhands, nplayers)


if __name__ == '__main__':
    main(sys.argv)
