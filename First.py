import numpy as np
board=np.zeros((3,3),dtype=int)
print(board)

def print_board(b):
    symbols={0:" ", 1:"X", -1:"O"}
    for r in range (3):
        row=" | ".join(symbols[val] for val in b[r])
        print(" "+row)
        if r<2:
            print("---+---+---")
    print()
def check_winner(b):
    if 3 in np.sum(b,axis=1) or 3 in np.sum(b,axis=0):
        return 'X'
    if -3 in np.sum(b,axis=1) or -3 in np.sum(b,axis=0):
        return 'O'
    if np.trace(b)==3 or np.trace(np.fliplr(b))==3:
        return 'X'
    if np.trace(b)==-3 or np.trace(np.fliplr(b))==-3:
        return 'O'
    if not 0 in b:
        return'DRAW'
    return None
current=1

print("welcome to the Tic Tac Toe Game")
while True:
    if current == 1:
        player='X'
    else  :
        player='O'
    try :    
        row=int(input(player+" - Enter the row(0,1,2):"))
        col=int(input(player+" - Enter the row(0,1,2):"))
    except ValueError:
        print("Enter the Valid Column") 
        continue
    if row <0 or row>2 or col >2 or col<0:
        print("row and cl must be between the 0 and 2")
        continue
    if board[row,col]!=0:
        print("Place is already filled")
        continue
    board[row,col]= current
    print_board(board)

    result = check_winner(board)
    if result is not None:

        if result == 'X':
            print("X wins the Game")
        if result =='O':
            print("O wins the Game")
        if result =='DRAW':
            print("IT's a Draw")        
        break
    if current==1:
        current=-1
    else:
        current =1 

            

         
print_board(board)           