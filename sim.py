"""
Raj simulation run
"""
from raj import Board, Player, RandBot, MinMaxBot
from operator import attrgetter


def human_v_robot():
  players = [Player('Eric')]
  players.append(RandBot('RandBot'))
  board = Board(players)
  results = board.run()
  exit()

def humans():
  PLAYERNAMES = ['Kevin', 'Bob', 'Alice']
  humans = [Player(x) for x in PLAYERNAMES]
  board = Board(humans)
  results = board.run()
  exit()

def main():

  scoreboard = {'RandBot': 0, 'RandBot2': 0, 'Minnie2': 0, 'RandBot3': 0}
  for i in range(1, 10000):
    bots = [RandBot('RandBot'), RandBot('RandBot2'), MinMaxBot('Minnie2'), RandBot('RandBot3')]
    board = Board(bots)
    results = board.run()
    winner = max(results, key=attrgetter('score'))
    scoreboard[winner.name] += 1

  print scoreboard

if __name__ == '__main__':
  main()
  #humans()
  #human_v_robot()
