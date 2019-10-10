# import MemoryGameGUI 

size = 5

def set_board(size):
    board = []
    i=-1
    for element in range(size):
        i =0
        board += [[str(i)]]
    for element in range(size-1):
        i+=1
        for element in range(size):
            board[element] += str(i)
    print(board)

def set_cards(cards,board2):
    i=-1
    board = []
    for element in range(board2):
        board += [[]]
    for element in range(board2):
        i += 1
        board[element] += cards[i]
        i+= 1
        board[element] += cards[i]
        i+= 1
        board[element] += cards[i]
        i+= 1
        board[element] += cards[i]
    print(board)

set_board(3)

set_cards(["a","b","c","d","e","f","g","h","i","j","k","l"],3)
