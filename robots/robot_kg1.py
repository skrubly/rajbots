"""KMG Robot 1."""

import copy
import random

from raj import Player

ROUND = 4

class KmgOneBot(Player):
  """Tries to compute the card to play.

  The idea:  Find the relative position of the current tile in the
  sorted list of remaining tiles.  Play a card from those I hold that
  has the same relative position.

  Something like that.
  """

  def __init__(self, name):
    """Initialize data."""

    Player.__init__(self, name)

  def find_rank(self, orig_tiles, orig_tile):
    """Find the rank of a tile in a list of tiles.

    Args:
      tiles: list of int.
      orig_tile: A Tile object or an int.
    Returns:
      A float which is the relative location of the tile between the
      max and min in the list.  The relative location is normalized to
      the range 0.0 to 1.0.
    """

    tiles = copy.copy(orig_tiles)

    if isinstance(orig_tile, int):
      tile = orig_tile
    else:
      tile = int(orig_tile.value)

    tiles.append(tile)

    max_val = max(tiles)
    min_val = min(tiles)

    if min_val == max_val:
      return 1.00

    rel_val = (tile - min_val) / float(max_val - min_val)

    return rel_val

  def rank_cards(self, cards):
    """Take a set of cards and return a dict with a rank value for each.

    Args:
      orig_cards: list of int.
    Returns:
      A dict with keys the rank of each card, and the value the original
      card.
    """

    ret_dict = {}
    for card in cards:
      rank = self.find_rank(cards, card)
      ret_dict[str(round(rank, 4))] = card

    return ret_dict

  def find_closest(self, value, orig_values):
    """In a list of values, find the one closest to value.

    Close means the smallest abs of the difference.

    Args:
      value: float.
      values: list of float.
    """

    values = copy.copy(orig_values)

    dist = 2.0
    close_value = None

    for a_value in values:
      a_value = float(a_value)
      new_dist = self.find_dist(a_value, value)
      if  new_dist < dist:
        close_value = a_value
        dist = new_dist

    return round(close_value, ROUND)

  def find_dist(self, value1, value2):
    """Find the distance between two floating point values.

    Args:
      value1: float.
      value2: float.
    Returns:
      The abs of the difference.
    """

    return abs(float(value1) - float(value2))

  def play_turn(self):
    """Play the turn."""

    current_tile = self.board.current_tile
    current_rank = self.find_rank(self.board.remaining_tiles,
                                  self.board.current_tile)

    # For the negative tile, we are trying to lose.
    # Also only use half of our cards for the range.
    if current_tile.value < 0:
      current_rank = 1.0 - current_rank
      current_rank = current_rank / 2
    else:
      current_rank = (1.0 + current_rank) / 2
      current_rank = (1.0 - current_rank) * 0.04 + current_rank

    # print 'Remaing cards:', self.board.remaining_tiles
    # print'Current tile, rank:', current_tile, current_rank

    cards_values = [int(x.number) for x in self.cards]
    # print 'Cards values:', cards_values

    values_to_cards = dict([(str(int(x.number)), x) for x in self.cards])
    ranks_of_cards = self.rank_cards(cards_values)
    closest_rank = self.find_closest(current_rank, ranks_of_cards.keys())

    final_value = ranks_of_cards[str(closest_rank)]
    final_card = values_to_cards[str(final_value)]
    # print
    # print 'Closest:', closest_rank, final_card

    return final_card
