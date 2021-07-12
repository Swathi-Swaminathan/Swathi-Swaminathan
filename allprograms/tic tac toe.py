#Python program for tic tac toe
def tictactoe():
    print("WELCOME")
    print("Game Started")
    play_again=True
    while play_again:
        
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player=1
        
        print("Player",player,"select your marker")
        marker=input()
        player_1 , player_2 = set_marker(marker)
        while True:
            if player > 2:
              player=1
            print("Player ",player,":Enter your position")
            pos = int(input())
            if check_pos(pos,board):
                continue
            if player == 1:
                set_board(board,player_1,pos)
            else:
                set_board(board,player_2,pos)
            display(board)
            if player == 1:
                if check_win(board,player_1):
                    print("Player ",player," has won...")
                    play_again=False
                    break
            else:
                if check_win(board,player_2):
                    print("Player ",player," has won^^^")
                    play_again=False
                    break
            if check_space(board):
                  print("Draw!!!")
                  play_again=False
                  break
            player+=1
            
        

def set_marker(marker):
    if marker=="X":
        return("X","O")
    else:
        return("O","X")
def check_pos(pos,board):
    if board[pos] == " ":
        return False
    else:
        return True
def set_board(board,marker,pos):
    board[pos] = marker
def display(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print("------------------")
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print("------------------")
    print(f'{board[6]} | {board[7]} | {board[8]}')
def check_win(board,marker):
    return board[0]==marker and board[1]==marker and board[2]==marker or board[4]==marker and board[5]==marker and board[3]==marker or board[7]==marker and board[8]==marker and board[6]==marker or board[6]==marker and board[3]==marker and board[0]==marker or board[1]==marker and board[4]==marker and board[7]==marker or board[2]==marker and board[3]==marker and board[8]==marker or board[0]==marker and board[4]==marker and board[8]==marker or board[2]==marker and board[4]==marker and board[6]==marker
def check_space(board):
    if " " in board:
        return False
    else:
        return True

      
tictactoe()

