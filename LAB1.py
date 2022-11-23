#tic tac toe using AI
player, computer = 'x', 'o'

def main():
    board = [
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]
    ]

    printBoard(board)
    print("At each turn enter your cell number")
    print("Cells are numbered from 1 to 9")
    
    choice = input("Do you want to play first?\n")
#    choice = 'n'
    if choice.lower() in ["yes", "y", "yeah"]:
        k = 0
        while(k <= 5):
            k += 1
            print("Your Turn:")
            cell = int(input("Cell Number: "))
            if(cell <= 0 or cell > 9):
                print("Enter a valid cell number")
                k -= 1
                continue
            cell -= 1
            i = cell // 3
            j = cell % 3
            if(board[i][j] != '_'):
                print("Cell occupied")
                k -= 1
                continue
            board[i][j] = player
            printBoard(board)
            if(evaluate(board) == 10):
                print("YOU WIN!!!")
                return
            if(k == 5 and evaluate(board) == 0):
                print("DRAW!!!")
                return
            print("Computer's Turn")
            bestMove = findBestMove(board)
            i = bestMove[0]
            j = bestMove[1]
            board[i][j] = computer
            printBoard(board)

            if(evaluate(board) == -10):
                print("YOU LOOSE!")
                return

    elif choice.lower() in ["no", "n", "nah"]:
        k = 0
        while(k < 5):
            k += 1
            print("Computer's Turn")
            bestMove = findBestMove(board)
            i = bestMove[0]
            j = bestMove[1]
            board[i][j] = computer
            printBoard(board)
            if(evaluate(board) == -10):
                print("YOU LOOSE!")
                return
            if(k == 4 and evaluate(board) == 0):
                print("DRAW!!!")
                return
            print("Your Turn:")
            while(True):
                cell = int(input("Cell Number: "))
                if(cell <= 0 or cell > 9):
                    print("Enter a valid cell number")
                    continue
                cell -= 1
                i = cell // 3
                j = cell % 3
                if(board[i][j] != '_'):
                    print("Cell occupied")
                    continue
                else:
                    break
            board[i][j] = player
            printBoard(board)
            if(evaluate(board) == 10):
                print("YOU WIN!!!")
                return
    else:
        print("GAME ENDS as you did not enter a valid choice")


def printBoard(b):
    for i in range(3):
        print(b[i])

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_'):
                return True
    return False

#evaluation function

def evaluate(b):
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player) :
                return 10
            elif (b[row][0] == computer) :
                return -10

    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2] [col]):
            if(b[0][col] == player):
                return 10
            elif (b[0][col] == computer):
                    return -10

    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if(b[0][0] == player):
            return 10
        elif (b[0][0] == computer) :
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if(b[0][2] == player):
            return 10
        elif (b[0][2] == computer) :
            return -10

    return 0

#this is the minimax function. t considers all the possible ways the game can go
#and returns the value of the board

def minimax(board, depth, isMax):
    score = evaluate(board)
    if (score == 10):
        return score
    elif (score == -10):
        return score

    if(isMovesLeft(board) == False) :
        return 0

    if (isMax) :
        best = -1000
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    board[i][j] = player
                    best=max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best-depth
      #  return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if(board[i][j] == '_'):
                    board[i][j] = computer
                    best=min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best+depth
##    return best
    
#this will return the best possible move for a computer

def findBestMove(board):
    bestVal = 1000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):

            if(board[i][j] == '_'):
                board[i][j] = computer
                moveVal = minimax(board, 0, True)
                board[i][j] = '_'
                #print("best val = ",bestVal)
                
                if(moveVal+10 < bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

main()