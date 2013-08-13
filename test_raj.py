"""
Unit tests for Raj
"""

from collections import defaultdict
from operator import attrgetter
from raj import Player, Board, RandBot

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

if __name__ == '__main__':
  DEBUG = False
  unittest.main()
