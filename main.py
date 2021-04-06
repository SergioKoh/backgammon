import root.board as bb
import options.optlev as oo
import counters.chip as cc
import players.player as pp
import watch.clock as wc
import dice.dice as dd
import scoring.scoreboard as ss


WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400


def main():
    board = bb.Board(WIDTH, HEIGHT, WIDTH_MIN, HEIGHT_MIN)
    board_points = board.draw_board()
    player_0 = pp.Player(0)
    player_1 = pp.Player(1)
    backgammon_clock = wc.Clock()
    create_chips(board_points)
    create_dice()
    scoreboard_0 = ss.Score(0)
    scoreboard_1 = ss.Score(1)
    options_toplevel= oo.OToplevel(board, WIDTH_MIN, HEIGHT_MIN)
    options = options_toplevel.splitting_segments()
    board.mainloop()

def create_chips(board_points):
    counters_0 = cc.Counters(0)
    counters_1 = cc.Counters(1)
    location_chips = [0] * 24
    counters_0.random_chips(location_chips)
    counters_1.random_chips(location_chips)
    counters_0.draw_chips(board_points, location_chips)
    counters_1.draw_chips(board_points, location_chips)

def create_dice():
    die_00 = dd.Dice(0, 0)
    die_01 = dd.Dice(0, 1)
    die_10 = dd.Dice(1, 0)
    die_11 = dd.Dice(1, 1)

if __name__ == '__main__':
    """"""
    main()
