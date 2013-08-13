"""
Robots for Raj tournaments 
"""

from raj import Player

class SampleBot(Player):
  # The only method you need to implement is play_turn
  def play_turn(self):
    """ 
    When it is your robots turn, this method will be called.
    It should return the Card object that you want to play.
    """
    return self.cards[-1]

class PatternBot(Player):
  """ Plays a pre-defined pattern based entirely on what tile is in play """
  def play_turn(self):
    playing_dict = { -5: 6,
                     -4: 5,
                     -3: 4,
                     -2: 3,
                     -1: 2,
                     1: 1,
                     2: 7,
                     3: 8,
                     4: 9,
                     5: 10,
                     6: 11,
                     7: 12,
                     8: 13,
                     9: 15,
                     10: 14}
    current_tile = self.board.current_tile
    return self.select_card(playing_dict[current_tile.value])
