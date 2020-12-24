import numpy as np


# Player colors
BLACK = -1
WHITE = 1


class Game:
    def __init__(self, width, height):
        # Who's the current player
        self.turn = np.random.choice([BLACK, WHITE])

        # Dimensionality
        self.width = width
        self.height = height

        # Board
        self.board = np.zeros((self.width, self.height))
        self.available = (None,
            np.zeros((self.width, self.height), dtype=bool), # Available white spots
            np.zeros((self.width, self.height), dtype=bool)  # Available black spots
        )

    def __getitem__(self, xy):
        x, y = xy
        return self.board[x][y]

    def __setitem__(self, xy, value):
        x, y = xy
        self.update(x, y, value)

    def update(self, x, y, value):
        self.board[x][y] = value
        
        # Do nothing if removing piece
        # TODO: Consider this later!
        if value == 0:
            return

        # Loop through all ---

        

    def is_connected(self, x, y):
        for px, py in self.get_hooks(x, y):
            if self[px, py] == self[px, py]:
                pass

    # Areas / Regions

    def affected(self, x, y):
        n = 3
        for i in range(-n, n + 1):
            spread = n - abs(i)
            for j in range(-spread, spread + 1):
                yield x + i, y + j