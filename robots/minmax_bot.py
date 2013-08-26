"""
Attempts to win every tile (including negatives) by playing its highest 
or lowest card. 
"""
from raj import Player


class MinMaxBot(Player):
  """ 
  MinMax will return its smallest or largest card, depending upon the current tile
  """

  def play_turn(self):
    if self.board.current_tile.value < 0:
      return self.cards[0]
    else:
      return self.cards[-1]
