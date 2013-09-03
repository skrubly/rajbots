"""A non-printing game board."""

import random
import raj
import sys


class Board(raj.Board):
  """A no-printing board."""

  def __init__(self, players, games_quantity=1):
    """Initialize a scoreboard that counts wins."""

    raj.Board.__init__(self, players, games_quantity)
    self.wins_board = self.init_scoreboard()

  def winner_name(self):
    """Return the name of the winner."""

    winning_score = 0
    winner_name = ''
    for name, score in self.scoreboard.items():
      if score > winning_score:
        winner_name = name
        winning_score = score

    return winner_name

  def round_winner_name(self):
    """Determine which player won this round."""

    winning_score = 0
    winner_name = ''
    for player in self.players:
      if player.score > winning_score:
        winner_name = player.name
        winning_score = player.score

    return winner_name

  def run_game(self):
    self.tilestack = [raj.Tile(x) for x in raj.TILE_VALUES]
    self.current_tile = None
    prize_stack = []
    while self.tilestack:
      round_log = {'prize': None, 'winner': None, 'pile': None}
      # self.print_scoreboard()
      self.current_tile = random.choice(self.tilestack)
      prize_stack.append(self.current_tile)
      self.tilestack.remove(self.current_tile)
      card_pile = []
      # print("\nCurrent tile: %s" % self.current_tile)
      for player in self.players:
        card_pile.append(player.play_turn())
      # print "Card pile: %s" % card_pile 
      round_log['pile'] = list(card_pile)
      #print "Prize stack: %s" % prize_stack
      # Determine the winner
      if self.current_tile.value < 0:
        winning_card = self.find_lowest(card_pile) 
      else:
        winning_card = self.find_highest(card_pile)
      if winning_card:
        # print "%s wins!" % winning_card.owner
        round_log['prize'] = list(prize_stack)
        round_log['winner'] = winning_card.owner
        winning_card.owner.tiles.extend(prize_stack)
        prize_stack = []
      else:
        pass
        # print "Prize rolls over!"
      # Now remove the cards from each players hand
      for card in card_pile:
        card.owner.cards.remove(card)
      # Add to the rounds log
      self.rounds.append(round_log)

    # print "Game over! Final scores:"
    for player in self.players:
      # print "%s: %s" % (player.name, player.score)
      self.scoreboard[player.name] += player.score
    # print "Log of the game:"
    # for entry in self.rounds:
      # print "Cards: %s Winner: %s Prize: %s" % (entry['pile'], entry['winner'], entry['prize'])
    #return self.players

    self.wins_board[self.round_winner_name()] += 1
      
    return self.rounds

  def run(self):
    while self.game_quantity > 0:
      self.games.append(self.run_game())
      # Reset the players cards and tilestacks
      for player in self.players:
        player.init_cards()
        player.tiles = []
      self.rounds = []
      self.game_quantity -= 1

      if not self.game_quantity % 100:
        sys.stdout.write('%d...' % self.game_quantity)
        sys.stdout.flush()

    print
