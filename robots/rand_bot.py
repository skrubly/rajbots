"""
Random Bot - plays a random card from its hand each turn.
"""
import random

from raj import Player

class RandBot(Player):
  def play_turn(self):
    return random.choice(self.cards)
