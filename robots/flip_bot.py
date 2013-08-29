"""
An example template for a robot
"""

from raj import Player

class FlipBot(Player):
  """ Flip Bot flips back and forth between playing its highest and lowest cards """
  def __init__(self, name):
    self.flip = 1
    super(FlipBot, self).__init__(name)

  def play_turn(self):
    card_number_to_play = 0

    if self.flip > 0:
      self.flip = -1
      card_number_to_play = self.held_cards[-1]
    else:
      self.flip = 1
      card_number_to_play = self.held_cards[0]
    return self.select_card(card_number_to_play)
