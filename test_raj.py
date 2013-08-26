"""
Unit tests for Raj
"""

from collections import defaultdict
from operator import attrgetter
from raj import Player, Board
from robots.rand_bot import RandBot

import unittest


def debug(text): 
  try:
    if DEBUG:
      print(text)
  except:
    pass

class TestPlayer(unittest.TestCase):
  def setUp(self):
    self.names = ['Alice', 'Bob']

  def test_create(self):
    self.players = [Player(x) for x in self.names]
    debug((self.players, self.names))
    self.assertEquals(self.names, [x.name for x in self.players])

  def test_held_cards(self):
    self.player = Player('Carl')
    debug(self.player.held_cards)
    self.assertEquals(self.player.held_cards, range(1, 16))

  def test_played_cards(self):
    self.player = Player('Dudley')
    self.player.cards.pop()
    debug(self.player.played_cards)
    self.assertEquals(self.player.played_cards, [15])


class TestRobot(unittest.TestCase):
  def setUp(self):
    self.robot = RandBot('RandBot')

  def test_play(self):
    choice = self.robot.play_turn()
    debug(self.robot.__dict__)
    debug(choice)
    self.assertEquals(type(choice.number), type(int()))

class TestSorting(unittest.TestCase):
  def setUp(self):
    self.names = ['Alice', 'Bob', 'Carl']
    self.players = [Player(x) for x in self.names]
    self.board = Board(self.players)

  def test_high_unique(self):
    self.pile = []
    self.pile.append(self.players[0].select_card(15))
    self.pile.append(self.players[1].select_card(15))
    self.pile.append(self.players[2].select_card(13))
    debug('Highest unique card: %s' % self.board.find_highest(self.pile))
    self.assertEqual(self.board.find_highest(self.pile).owner.name, 'Carl')

  def test_low_unique(self):
    self.pile = []
    self.pile.append(self.players[0].select_card(1))
    self.pile.append(self.players[1].select_card(1))
    self.pile.append(self.players[2].select_card(3))
    debug('Lowest unique card: %s' % self.board.find_lowest(self.pile))
    self.assertEqual(self.board.find_lowest(self.pile).owner.name, 'Carl')

  def test_tied(self):
    """ Test for a tie when all cards are the same """
    self.pile = []
    self.pile.append(self.players[0].select_card(15))
    self.pile.append(self.players[1].select_card(15))
    self.pile.append(self.players[2].select_card(15))
    self.assertEqual(self.board.find_highest(self.pile), None)

class TestPlay(unittest.TestCase):
  def setUp(self):
    self.names = ['Alice', 'Bob', 'Carl']
    self.players = [RandBot(x) for x in self.names]
    self.board = Board(self.players)

  def test_playthrough(self):
    self.board.run()
    print self.board.games

if __name__ == '__main__':
  DEBUG = False
  unittest.main()
