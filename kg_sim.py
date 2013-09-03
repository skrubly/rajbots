#!/usr/bin/env python

"""
Raj simulation run
"""

import sys

from raj import Board, Player
from robots.sample_bot import SampleBot
from robots.pattern_bot import PatternBot
from robots.rand_bot import RandBot
from robots.minmax_bot import MinMaxBot
from robots.flip_bot import FlipBot
from robots.robot_kg1 import KmgOneBot
import board_kg


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
  bots = [RandBot('Alice'), PatternBot('Bob'), RandBot('Carl'),
          KmgOneBot('Ken')]
  board = Board(bots, 30)
  board.run() 
  print board.scoreboard

def lots_robots(run_count):
  bots = [RandBot('Alice'),
          PatternBot('Bob'),
          RandBot('Carl'),
          FlipBot('Dave'),
          KmgOneBot('Ken'),
          ]
  board = board_kg.Board(bots, run_count)
  board.run()

  return board.wins_board


if __name__ == '__main__':
  # robots()
  # human_v_robot()
  # humans()
  wins = lots_robots(500)

  print wins

