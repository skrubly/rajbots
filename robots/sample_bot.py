"""
An example template for a robot
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
