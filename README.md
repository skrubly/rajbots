# rajbots

A simulator for exploring strategies in the boardgame Raj/Hol's der Geier. 

For information and rules see the Boardgame Geek page for [Raj](http://boardgamegeek.com/boardgame/175/raj)

## Installation

Everything is designed to run out of the rajbots directory. A simple git clone of https://github.com/skrubly/rajbots will work.


## Running the Simulator

sim.py is a simple script for starting a game session simulation. You'll find three examples of how to run simulations between Human vs Robot, just Humans, and just Robots. Each shows how to create a Board object and populate it with Players. 

### Robots

There are premade robots located in the robots/ subdirectory. Here's a brief overview of what they do:

  * RandBot - Plays a random card from its hand each turn.
  * MinMaxBot - Plays either the highest or lowest card, depending on the tile value.
  * PatternBot - Plays a predefined card based upon tile value.
  * SampleBot - Useful as a template for your own robot, plays the highest card it has.

## Writing Robots

As can be seen in the examples, a basic robot is extremely simple to create. The only method that a robot has to support is `play_turn`, which is called by the Board object. To create a robot that does something more than play random cards will require gathering information about the game - the current tile being bid on, what tiles are left, and which cards have been played. The Board object provides methods to discover all of the information available in the game. But first, let's look at what methods exist on a Player object.

### The Player Object

Every robot should subclass Player, and at the least should override the `play_turn` method as shown in SampleBot. The following information is available from the Player object:

#### Attributes

  * `name` - The given name of that Player instance. 
  * `cards` - A list of Card objects currently held by the player
  * `tiles` - A list of Tile objects the player has won
  * `score` - A property that returns the sum of all of the Tiles held by the player
  * `held_cards` - A property that returns an integer list of cards the player holds
  * `played_cards` - A property that returns an integer list of cards the player has already played

#### Methods
  * `select_card(card_number)` - The method used to return a Card object based on its number. `card_number` should be an integer

The Player object provides a lot of potential sources of strategy or tactical information.  One of the obvious helpers is knowing the highest card an opponent has yet to play. But how to access this information during the game? We gain this information through the Board object.

### The Board Object

The Board object is the container for the entire game and holds all information regarding players and what has happened so far. 

#### Attributes

  * `players` - The list of Player objects participating in the game
  * `rounds` - For the current game, a log of each round of play.
  * `games` - Holds the total list of round logs (for when you play a series of games)
  * `scoreboard` - A dict, the accumulated score for all rounds played so far.
  * `game_quantity` - The number of games to be played 
  * `current_tile` - The current tile being bid on 
  * `tilestack` - The stack of tile objects yet to be played
  * `remaining_tiles` - Property that returns a list of integers of the tiles in the stack

Using the board object to gather information about the game is straightforward. Let's see what these attributes look like midway through a hypothetical game between Alice, Bob, and Carl.

We will be imaginative and call our Board object `board`.

    print(board.players)
    [Alice, Bob, Carl]

Let's take a peek and see what cards Alice is holding:

    print(board.players[0].held_cards)
    [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14]

Looks like she's missing her 8 and 15. But, we could tell that easier by looking at her played cards:

    print(board.players[0].played_cards)
    [8, 15]

So, we know that Alice isn't going to be able to play a 15, because she's already played it. 

    print(board.remaining_tiles)
    [-5, -4, -3, -2, 1, 2, 3, 4, 6, 7, 8, 9, 10]

So -1 and 5 have already been bid on and won. To get a list of dicts of the gamelog so far, access board.rounds:

    print(board.rounds)
    [{'winner': Bob, 'pile': [Alice:8, Bob:4, Carl:5], 'prize': [-1]},
     {'winner': Alice, 'pile': [Alice:15, Bob:14, Carl:11], 'prize': [5]}]

Here we see a list of each round in sequence, who played what, and who won the prize, along with its value.

Between examining information about other players and what cards they hold, and even in how they played previously, a fairly sophisticated robot could be constructed.



## TODO

  * An example of a slightly more sophisticated robot
  * More unit tests!
