"""
RandomBot -- A simple strategy: enumerates all legal moves, and picks one
uniformly at random.
"""

# Import the API objects
from api import State
import random


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        # All legal moves
        moves = state.moves()

        if moves:
            try:
                moves.sort(key=lambda move:move[0])
                max_move = max(moves)
            except:
                max_move = moves[-1]
        else:
            max_move = random.choice(moves)

        return max_move
