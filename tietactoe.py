import random
board = [0,1,2,
         3,4,5,
         6,7,8]

def show():
    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print('---------')
    print(board[6],'|',board[7],'|',board[8])

def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True
def checkAll(char):
    #Horizontal
    if checkLine(char, 0,1,2):
        return True
    if checkLine(char, 3,4,5):
        return True
    if checkLine(char, 6,7,8):
        return True

    #vertical
    if checkLine(char, 1,4,7):
        return True
    if checkLine(char, 2,5,8):
        return True
    if checkLine(char, 0,3,6):
        return True

    #Diagonals
    if checkLine(char, 0,4,8):
        return True
    if checkLine(char, 2,4,6):
        return True
def GameTie():
    if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] == 'X' or board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] == 'O':
        print("Game Tie")
        return True

while True:
    try:
        inputt=int(input("1st Player Select a spot:"))
        if board[inputt]!= 'X' and board[inputt]!= 'O':
            board[inputt]= 'X'
            show()

            if checkAll('X') == True:
                print("---1st Player wins--")
                show()
                break
            #We put GameTie here bcz last choice is made by X(1st player) then it will tie
            elif GameTie() == True:
                break
            #Check the taken spots
            while True:
                try:
                    opponent = int(input('2nd Player Select a spot:'))
                    if board[opponent] != 'X' and board[opponent] != 'O':
                        board[opponent] = 'O'

                        if checkAll('O') == True:
                            print("---2nd Player wins--")
                            show()
                            exit() #If we put break then it will continue bcz of 2 loops , break will break first loop but not 2nd loop

                        show()
                        break
                    else:
                        print('This spot is taken!')
                except Exception as e:
                    print('Wrong Input')
        
        else:
            
            print('This spot is taken!')

    except Exception as e:
        print('Wrong Input')
        
