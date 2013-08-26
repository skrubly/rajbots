"""
Raj simulation run
"""
from raj import Board, Player
from robots.sample_bot import SampleBot
from robots.pattern_bot import PatternBot
from robots.rand_bot import RandBot
from robots.minmax_bot import MinMaxBot


def human_v_robot():
  players = [Player('Eric'), RandBot('RandBot')]
  board = Board(players)
  board.run()
  print board.scoreboard

def humans():
  PLAYERNAMES = ['Kevin', 'Bob', 'Alice']
  humans = [Player(x) for x in PLAYERNAMES]
  board = Board(humans)
  board.run()
  print board.scoreboard

def robots():
  bots = [RandBot('Alice'), PatternBot('Bob'), RandBot('Carl')]
  board = Board(bots, 30)
  board.run() 
  print board.scoreboard

if __name__ == '__main__':
  robots()
  #human_v_robot()
  #humans()
