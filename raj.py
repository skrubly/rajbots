"""
Simple python game of Raj
"""

import random

from collections import defaultdict
from operator import attrgetter

TILE_VALUES = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#TILE_VALUES = [-5, 4]


class Card(object):
  def __init__(self, number, owner):
    self.number = number
    self.owner = owner
  
  def __str__(self):
    return str(self.number)

  def __repr__(self):
    return '%s:%s' % (self.owner, self.number)

class Tile(object):
  def __init__(self, value):
    self.value = value
    self.owner = None

  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return str(self.value)


class Player(object):
  def __init__(self, name):
    self.name = name
    self.tiles = []
    self.cards = [Card(x, self) for x in range(1, 16)]
    self.winner = False

  @property
  def score(self):
    return sum([x.value for x in self.tiles])

  def select_card(self, number):
    chosen_card = None
    for card in self.cards:
      if card.number == number:
        chosen_card = card
    return chosen_card

  def play_turn(self):
    valid_choice = False
    while not valid_choice:
      choice = raw_input("%s Card Choices: %s" % (self.name, 
                                                  [x.number for x in self.cards]))
      try:
        if int(choice) in [x.number for x in self.cards]:
          valid_choice = self.select_card(int(choice))
        else:  
          pass
      except:
        continue
    return valid_choice

  def __str__(self):
    return self.name
    #return self.name + ":" + str(self.score)

  def __repr__(self):
    return self.name


class Board(object):
  def __init__(self, players):
    self.players = players
    self.tilestack = [Tile(x) for x in TILE_VALUES]
    self.current_tile = None
    self.rounds = []
    for player in self.players:
      player.board = self
    
  def find_lowest(self, pile):
    """ Find the lowest unique card on the pile """
    histo_dict = defaultdict(list)    
    for item in pile:    
      histo_dict[item.number].append(item)    
    try:
      lowest = min([y[0] for (x, y) in histo_dict.items() if len(y) == 1], 
                     key=attrgetter('number')) 
    except ValueError:
      return None
    return lowest

  def find_highest(self, pile):
    """ Find the highest unique card on the pile """
    histo_dict = defaultdict(list)    
    for item in pile:    
      histo_dict[item.number].append(item)    
    try:
      highest = max([y[0] for (x, y) in histo_dict.items() if len(y) == 1], 
                     key=attrgetter('number')) 
    except ValueError:
      return None
    return highest

  def print_scoreboard(self):
    print "Scores:"
    for player in self.players:
      print "\t%s: %s" % (player.name, player.score)

  def run(self):
    prize_stack = []
    while self.tilestack:
      round_log = {'prize': None, 'winner': None, 'pile': None}
      self.print_scoreboard()
      self.current_tile = random.choice(self.tilestack)
      prize_stack.append(self.current_tile)
      self.tilestack.remove(self.current_tile)
      card_pile = []
      print("Current tile: %s" % self.current_tile)
      for player in self.players:
        card_pile.append(player.play_turn())
      print "Card pile: %s" % card_pile 
      round_log['pile'] = list(card_pile)
      #print "Prize stack: %s" % prize_stack
      # Determine the winner
      if self.current_tile.value < 0:
        winning_card = self.find_lowest(card_pile) 
      else:
        winning_card = self.find_highest(card_pile)
      if winning_card:
        print "%s wins!" % winning_card.owner
        round_log['prize'] = list(prize_stack)
        round_log['winner'] = winning_card.owner
        winning_card.owner.tiles.extend(prize_stack)
        prize_stack = []
      else:
        print "Prize rolls over!"
      # Now remove the cards from each players hand
      for card in card_pile:
        card.owner.cards.remove(card)
      # Add to the rounds log
      self.rounds.append(round_log)

    print "Game over! Final scores:"
    for player in self.players:
      print "%s: %s" % (player.name, player.score)
    print "Log of the game:"
    for entry in self.rounds:
      print "Cards: %s Winner: %s Prize: %s" % (entry['pile'], entry['winner'], entry['prize'])
    return self.players


class RandBot(Player):
  #def __init__(self):
  #  super(RandBot, self).__init__(name='RandBot')
  def play_turn(self):
    return random.choice(self.cards)

class MinMaxBot(Player):
  """ MinMax will return its smallest or largest card, depending upon the current tile """
  def play_turn(self):
    if self.board.current_tile.value < 0:
      #print "LESS THAN 0: %s" %  self.cards[0]
      return self.cards[0]
    else:
      #print "MORE THAN 0: %s" % self.cards[-1]
      return self.cards[-1]

