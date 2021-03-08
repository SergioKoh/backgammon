""" Less than 0 black chips,
    greater than 0 white chips,
    0 no chip position,
    26 position bar black,
    27 position bar white.
    In the list is the starting position of the game.
"""
counters = [0, 0, -2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, -5, 0, 0, 0, 0, 2, 0, 0, 0]

class Counter:
    """"""
    def __init__(self, color):
        self.color = color
#        self.position

    def knock_chip(self):
        """A chip knocks someone else's chip into the bar"""
        pass
