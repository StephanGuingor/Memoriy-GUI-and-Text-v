from MEM import *

cards_list = ["Spade","Spade","Ace","Ace","Dart","Dart","Computer","Computer","Smok","Smok","Book","Book","Alfa","Alfa","Red","Red"]
shuffle(cards_list)
art = "X_X"

rules = "If you want to quit, just type quit instead of choosing your column and row.\nEither way, have fun!"
cards = Cards(cards_list,art)
memory_board = Board(cards,rules)

memory_board.print_draw(cards)