import board.board as bb
import options.optlev as oo
import counters.chip as cc
import players.player as pp
import watch.timer as wt


WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400


def main():
    player_0 = pp.Player(0)
    player_1 = pp.Player(1)
    board = bb.Board(WIDTH, HEIGHT)
    board_points = board.draw_board()
    timer = wt.Timer()
    counters_0 = cc.Counters(0)
    counters_1 = cc.Counters(1)
    location_chips = [0] * 24
    counters_0.random_chips(location_chips)
    counters_1.random_chips(location_chips)
    counters_0.draw_chips(board_points, location_chips)
    counters_1.draw_chips(board_points, location_chips)
    options_toplevel= oo.OToplevel(board, WIDTH_MIN, HEIGHT_MIN)
    options = options_toplevel.splitting_segments()


    board.mainloop()



if __name__ == '__main__':
    """"""
    main()
