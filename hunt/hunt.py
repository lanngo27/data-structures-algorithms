'''
In this exercise, we’re building a solving algorithm for an old-school back-to-basics computer game.
    It’s a very simple text based adventure game where you walk around and try to find treasures, while avoiding traps.
    The game is played on a rectangular, two dimensional grid.

    The game will consist of the player moving around on the grid for as long as they like (or until they fall into a trap).
    The player can move up, down, left and right (but not diagonally).
    If the player enters a square containing gold, the gold is picked up.
    If the player stands next to (i.e., immediately up, down, left, or right of) one or more traps, they will "sense a draft" but do not know from what direction the draft comes, or how many traps are near.
    It is not possible to enter squares which contain walls.
    Squares which contain walls or traps can never contain gold, i.e. all gold is positioned on normal floor tiles.
    Player cannot see gold from neighbouring squares.  

    For scoring purposes, we want to show the player how much gold they could have gotten safely.
    That is, how much gold can a player get playing with an optimal strategy and always being sure that the square they walked into was safe.
    '''

def safe_gold(level_string):
    """
    Starting from tile 'P' in level_string, calculate and return the amount of safe gold which can be collected.
    """

    gold = 0
    raise NotImplementedError("Gold hunting algorithm not yet implemented.")
    return gold
