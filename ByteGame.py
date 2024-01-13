import sys
import string
import copy

current = 'X'
#firstPlayer = 0
winner = ''
matrix = []
n = 0 # nxn dimenzije table
direction = ['GL', 'GD', 'DL', 'DD']
resultX=0
resultO=0
computer = False

def init():
    global matrix
    global n
    print("Dimenzija tabele: ")
    n = int(sys.stdin.readline())
    if (n%2!=0):
        print("Dimenzija tabele treba da bude parna.")
        return False
    elif ((((n/2)*(n-2))%8)!=0):
        print("Broj figura na tabli mora biti deljiv sa 8.")
        return False
    elif (n>16):
        print("Dimenzija tabele ne sme biti veca od 16.")
        return False
    else:
        matrix = [[list() for i in range(int(n/2))] for j in range(n)]
    for i in range(0, n): 
        for j in range(0, int(n/2)): 
            if (i != 0 and i != n-1): 
                if (i % 2 == 0):
                    matrix[i][j].append('O')
                else:
                    matrix[i][j].append('X')
    return True

def header(n):
    print('    ',end='')
    for num in range(0,n):
        if(num<8):
            print(''+ str(num+1),end='      ')
        else:
            print(''+ str(num+1),end='     ')
    print('') 

def table(board):
    global n, resultX, resultO
    header(n)
    for x in range(0,n):
        if (x%2==0):
            row=9
            while(row>0):
                if(row==6):
                    print(string.ascii_uppercase[x], end=' ') #/////////////
                else:
                    print('  ', end='') #////////////////////////
                for y in range(0,int(n/2)):                      
                    if (len(board[x][y])==0):
                        print('. . .', end='   ') #crno
                        print('   ',end='   ') #belo
                    else:
                        if (len(board[x][y])>row-3 and len(board[x][y])<=row):
                            for el in range(row-3, len(board[x][y])):
                                print(f'{board[x][y][el]}', end=' ')
                            for el in range(len(board[x][y]),row):
                                print('.', end=' ')
                            #print('6 . .', end='   ') #crno
                            print('',end='  ')
                            print('   ',end='   ') #belo
                        elif (len(board[x][y])>row):
                            for el in range(row-3, row):
                                print(f'{board[x][y][el]}', end=' ')
                            #print('6 . .', end='   ') #crno
                            print('',end='  ')
                            print('   ',end='   ') #belo
                        else:
                            print('. . .', end='   ') #crno
                            print('   ',end='   ') #belo
                print('')

                row-=3

        else:
            row=9
            while(row>0):
                if(row==6):
                    print(string.ascii_uppercase[x], end='  ') #/////////////
                else:
                    print('   ', end='') #////////////////////////
                for y in range(0,int(n/2)):                      
                    if (len(board[x][y])==0):
                        print('   ',end='   ')
                        print('. . .', end='   ') #crno
                        #print('   ',end='   ') #belo
                    else:
                        if (len(board[x][y])>row-3 and len(board[x][y])<=row):
                            print('   ',end='   ')
                            for el in range(row-3, len(board[x][y])):
                                print(f'{board[x][y][el]}', end=' ')
                            for el in range(len(board[x][y]),row):
                                print('.', end=' ')
                            #print('   ',end='   ')
                            #print('. . .', end='   ') #crno
                            print('',end='  ')
                            #print('   ',end='   ') #belo
                        elif (len(board[x][y])>row):
                            print('   ',end='   ')
                            for el in range(row-3, row):
                                print(f'{board[x][y][el]}', end=' ')
                            #print('6 . .', end='   ') #crno
                            print('',end='  ')
                            #print('   ',end='   ') #belo
                        else:
                            print('   ',end='   ')
                            print('. . .', end='   ') #crno
                            #print('   ',end='   ') #belo
                    
                print('')

                row-=3
    print('')
    print('X: '+str(resultX), end='    ')
    print('O: '+str(resultO))

def isFirstToPlay():

    #global firstPlayer
    global current, computer

    print("Da li prvo igrate vi ili racunar? (0-vi, 1-racunar)")
    computer = bool(int(sys.stdin.readline()))

    print("Ko igra prvi X ili O? (0-X, 1-O):")
    firstPlayer = int(sys.stdin.readline())
    if(firstPlayer==0):
        print("X je prvi na potezu.")
    else:
        print("O je prvi na potezu.")
        current = 'O'

    #print("Da li zelite da budete X ili O?")
    #current = sys.stdin.readline()

def checkIfFieldExists (i, j):
    row = ord(i) - 65
    column = j - 1
    if (row >= n or column >= n):
        #print ("Polje ne postoji na tabli")
        return False 
    return True
 
def checkIfFieldIsFilled(i, j):
    row = ord(i) - 65
    column = j - 1
    isFilled = False 
    for x in matrix[row][int(column/2)]:
        if(x == 'X' or x == 'O'):
            isFilled = True
    if(isFilled == False):
        #print('Polje je prazno.')
        return False    
    return True
    
def checkFigureAtIndex(i, j, index):
    row = ord(i)-65
    column = j - 1
    square = matrix[row][int(column/2)]
    if (len(square) <= index):
        #print("Mesto u polju koje ste zadali je prazno.")
        return False   
    return True
    
def checkDirection(dir):
    global direction
    correctDir = False
    for d in direction:
        if (dir == d):
            correctDir = True
    #if (correctDir == False):
        #print("Uneli ste nevalidnu vrednost za smer.")
    return correctDir

#funkcija koja proverava da li je polje gore levo prazno
def checkAdjacentUpperLeftField(i, j, board):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True

    if (row > 0 and column > 0):      
        if (row % 2 != 0):
            goreLevo = board[row - 1][int(column/2)] 
        else:
            goreLevo = board[row - 1][int((column - 1)/2)]  
        if len(goreLevo) != 0:     
            #print(f"Polje gore levo [{i}][{j}] nije prazno polje.")
            prazno = False 
    return prazno

#funkcija koja proverava da li je polje gore desno prazno
def checkAdjacentUpperRigtField(i, j, board):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True
 
    if (row > 0 and column < n - 1):      
        if (row % 2 != 0):
            goreDesno = board[row - 1][int((column + 1)/2)] 
        else:
            goreDesno = board[row - 1][int(column/2)]  
        if len(goreDesno) != 0:     
            #print(f"Polje gore desno [{i}][{j}] nije prazno polje.")
            prazno = False  
    return prazno

# funkcija koja proverava da li je polje dole desno prazno
def checkAdjacentLowerRightField(i, j, board):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True

    if (row < n - 1 and column < n - 1): 
        if(row % 2 != 0):
            doleDesno = board[row + 1][int((column + 1)/2)]  
        else:
            doleDesno = board[row + 1][int(column/2)]
        if len(doleDesno) != 0:
            #print(f"Polje dole desno [{i}][{j}] nije prazno polje.")
            prazno = False  
    return prazno

# funkcija koja proverava da li je polje dole levo prazno
def checkAdjacentLowerLeftField(i, j, board):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True

    if (row < n - 1 and column > 0): 
        if(row % 2 != 0):
            doleLevo = board[row + 1][int(column/2)]  
        else:
            doleLevo = board[row + 1][int((column - 1)/2)]
        if len(doleLevo) != 0:
            #print(f"Polje dole levo [{i}][{j}] nije prazno polje.")
            prazno = False 

    return prazno

def newPostionOfFigure(i, j, dir):
    
    global n
    row = ord(i) - 65
    column = j - 1
    
    nextStep = ()
    if(dir == 'GL'):
        if(row % 2 != 0):
            nextStep = (row-1, int(column/2))
        else:
            nextStep = (row-1, int((column-1)/2))
    if(dir == 'GD'):
        if(row % 2 != 0):
            nextStep = (row-1, int((column+1)/2))
        else:
            nextStep = (row-1, int(column/2))
    if(dir == 'DD'):
        if(row % 2 != 0):
            nextStep = (row+1, int((column+1)/2))
        else:
            nextStep = (row+1, int(column/2))
    if(dir == 'DL'):
        if(row % 2 != 0):
            nextStep = (row+1, int(column/2))
        else:
            nextStep = (row+1, int((column-1)/2))

    return nextStep

def checkAdjacentFields(i, j, dir, board):
        valid = False
        if (dir == "GL" and (checkAdjacentUpperLeftField(i, j, board) == False)):
            valid = True
        if (dir == "GD" and (checkAdjacentUpperRigtField(i, j, board) == False)):
            valid = True
        if (dir == "DL" and (checkAdjacentLowerLeftField(i, j, board) == False)):
            valid = True
        if (dir == "DD" and (checkAdjacentLowerRightField(i, j, board) == False)):
            valid = True
    
        if(checkAdjacentLowerRightField(i, j, board) and checkAdjacentLowerLeftField(i, j, board) 
           and checkAdjacentUpperRigtField(i, j, board) and checkAdjacentUpperLeftField(i, j, board)):
            valid = True
        return valid

def checkIfLeadsToClosestStack(i, j, dir, board):
    global n
    row = ord(i) - 65
    column = j - 1
    currStep = (row, int(column/2))
    allDistance = []
    allDir = []
    minDistance = float('inf')
    #print("Curent pos " + str(currStep))
    #print("Next pos " + str(nextStep))

    for d in direction:
        if(currStep[0] == 0 and (d == 'GL' or d == 'GD')):
            continue
        if(currStep[0] == n-1 and (d == 'DL' or d == 'DD')):
            continue
        if(currStep[1] == 0 and (d == 'GL' or d == 'DL')):
            continue
        if(currStep[1] == n-1 and (d == 'GD' or d == 'DD')):
            continue
        nextStep = newPostionOfFigure(i, j, d)
        for ind1 in range(0,n):
            for ind2 in range(0,int(n/2)):
                if(len(board[ind1][ind2])!=0 and currStep != (ind1, ind2)):
                    stack = (ind1, ind2)
                    newDistance = distance(nextStep, stack)
                    # currDistance = distance(stack, currStep)
                    allDistance.append(newDistance)
                    allDir.append(d)
                    if(newDistance < minDistance):
                        minDistance = newDistance
                    # print(f"Curr {currDistance} {stack[0]},{stack[1]*2} {currStep[0]},{currStep[1]*2}")
                    #print(minDistance)
    for index, i in enumerate(allDistance):
        if(i == minDistance and allDir[index] == dir):
            return True
                
    return False

def distance(pos1, pos2):
    # Manhattan distance |x1-x2|+|y1-y2|
    #return abs(pos1[0] - pos2[0]) + abs(pos1[1]*2 - pos2[1]*2)
    #return int(math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1]*2 - pos1[1]*2)**2))
    val1 = None
    val2 = None
    if(pos1[0] % 2 == 0):
        val1 = pos1[1]*2
    else:
        val1 = pos1[1]*2+1
    if(pos2[0] % 2 == 0):
        val2 = pos2[1]*2
    else:
        val2 = pos2[1]*2+1
    dist = max(abs(pos1[0] - pos2[0]), abs(val1 - val2))
    #print(f"New {dist} {pos1[0]},{val1} {pos2[0]},{val2}")
    return dist

def checkHeightOfStacks(i, j, index ,dir, board):
    global n

    position = newPostionOfFigure(i,j,dir)
    nextStep = board[position[0]][position[1]]
    #print(nextStep)
    nextStepHeight = len(nextStep)
    if (nextStepHeight <= index and nextStepHeight > 0):
        #print("Novi idex "+str(nextStepHeight)+" stari "+str(index))
        return False
    #print("Novi idex "+str(nextStepHeight)+" stari "+str(index))
    return True

def isGood(i, j, index, dir, board):
    global n
    row = ord(i)-65
    column = j - 1
    nextPosition = newPostionOfFigure(i,j,dir)
    nextStep = board[nextPosition[0]][nextPosition[1]]
    currStep = board[row][int(column/2)]

    if(checkAdjacentFields(i, j, dir, board)):
        if(checkIfLeadsToClosestStack(i, j, dir, board)):
            if(checkHeightOfStacks(i, j, index, dir, board)):
                #dodatak
                if(len(currStep) - index + len(nextStep) < 9):
                    return True
    return False
    
def isValid(i, j, index, dir, board, player):
    global n
    row = ord(i)-65
    column = j - 1
    #dodatak
    if(index >= len(board[row][int(column/2)])):
        return False
    if(row % 2 == 0 and column % 2 != 0):
        return False
    if(row % 2 !=0 and column % 2 == 0):
        return False
    if(board[row][int(column/2)][index] != player):
        return False
    if(row == 0 and (dir == 'GL' or dir == 'GD')):   
        return False
    if(row == n-1 and (dir == 'DL' or dir == 'DD')):
        return False
    if(column == 0 and (dir == 'GL' or dir == 'DL')):
        return False
    if(column == n-1 and (dir == 'GD' or dir == 'DD')):
        return False

    #proveriti da li zadato polje postoji na tabli
    if (checkIfFieldExists(i, j)):
        #proveriti da li postoje figure na zadatom polju
        if(checkIfFieldIsFilled(i, j)):
            #proveriti da li postoji figura na zadatom mestu na steku na zadatom polju  
            if(checkFigureAtIndex(i, j, index)): 
                #proveriti da li je smer jedan od cetiri moguca
                if(checkDirection(dir)):
                    
                    return True
    
    return False

def play(board, move):
    row= ord(move[0]) - 65
    column=move[1]-1
    index = move[2]
    dir = move[3]

    newBoard = [row.copy() for row in board]
    
    element = list()
    for x in range(index, len(newBoard[row][int(column/2)])):
        element.append(newBoard[row][int(column/2)][x])
    
    if(dir == 'DD'):
        for x in range(0, len(element)):
            if(column % 2 == 0):
                newBoard[row+1][int(column/2)].append(element[x])
            else:
                newBoard[row+1][int(column/2)+1].append(element[x])
    elif(dir == 'GD'):
        for x in range(0, len(element)):
            if(column % 2 == 0):
                newBoard[row-1][int(column/2)].append(element[x])
            else:
                newBoard[row-1][int(column/2)+1].append(element[x])
    elif(dir == 'GL'):
        for x in range(0, len(element)):
            if(column % 2 == 0):
                newBoard[row-1][int(column/2)-1].append(element[x])
            else:
                newBoard[row-1][int(column/2)].append(element[x])
    else:
        for x in range(0, len(element)):
            if(column % 2 == 0):
                newBoard[row+1][int(column/2)-1].append(element[x])
            else:
                newBoard[row+1][int(column/2)].append(element[x])

    for x in element:
        newBoard[row][int(column/2)].remove(x)

    #checkStack(newBoard)
    return newBoard

def checkStack(board, x, o):
    global n

    for i in range(0,n):
        for j in range(0,int(n/2)):
            if(len(board[i][j]) == 8):
                if(board[i][j][7] == 'X'):
                    x+=1
                    board[i][j].clear()
                else:
                    o+=1
                    board[i][j].clear()

    return [x,o]


def endGame():
    global resultX
    global resultO
    global winner
    global n

    stackNum = int(((n/2)*(n-2))/8)
    if(resultX>int(stackNum/2)):
        winner = 'X'
        return True 
    elif(resultO>int(stackNum/2)):
        winner = 'O'
        return True
    else: 
        return False

def start():

    global current, matrix, resultX, resultO
    isFirstToPlay()
    if (init()):
        table(matrix)
        while(True):

            if(endGame()):
                print("Kraj igre! Pobednik je: " + winner)
                break
            
            #showAllPossibleMoves(matrix, current)
            #showGameStateBasedOnPossibleMove(matrix, current)
            #print(f"{i}{j}{index}{dir}")
            
            if(computer):
                board = copy.deepcopy(matrix)
                move = minimaxBestMove(board)#...........
                if(move == None):
                    switchPlayer()
                    continue
                matrix = play(matrix, move)
                [resultX, resultO] = checkStack(matrix, resultX, resultO)
                table(matrix)
            else:
                moves = allGoodMoves(matrix, current)
                if(moves == None):
                    switchPlayer()
                    continue
                i = input("Unesite vrstu polja na kom se figura nalazi: ")
                j = input("Unesite kolonu polja na kom se figura nalazi: ")
                index = input("Unesite indeks figure u polju: ")
                dir = input("Unesite smer u kom zelite da pomerite figuru: ")
                move = [ i , int(j), int(index), dir]
                if(isValid(i,int(j),int(index), dir, matrix, current) and isGood(i,int(j),int(index), dir, matrix)):
                    matrix = play(matrix, move)
                    [resultX, resultO] = checkStack(matrix, resultX, resultO)
                    table(matrix)
                else:
                    print("Niste uneli validan potez!")
                    continue
            #print(evaluate(matrix, current))
            switchPlayer()
            print("Na potezu je: " + current)
    else:
        return False
    
def switchPlayer():
    global current, computer
    current = 'O' if current == 'X' else 'X'
    computer = False if computer else True

def allPossibleMoves(state, player):
    global n
    goodMoves = []
    badMoves = []
    for i in range(0,n):
        for j in range(0,int(n/2)):
            for index, value in enumerate(state[i][j]):      
                if(value == player):
                    
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'GL', state, player)):
                            if(isGood(chr(i+65),j*2+1,index,'GL', state)):
                                goodMoves.append([chr(i+65),j*2+1,index,'GL'])
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'GL'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'GL', state, player)):
                            if(isGood(chr(i+65),j*2+2,index,'GL', state)):
                                goodMoves.append([chr(i+65),j*2+2,index,'GL'])
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'GL'])
                    #######################################################
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'GD', state, player)):
                            if(isGood(chr(i+65),j*2+1,index,'GD', state)):
                                goodMoves.append([chr(i+65),j*2+1,index,'GD'])
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'GD'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'GD', state, player)):
                            if(isGood(chr(i+65),j*2+2,index,'GD', state)):
                                goodMoves.append([chr(i+65),j*2+2,index,'GD'])
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'GD'])
                    ####################################################
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'DD', state, player)):
                            if(isGood(chr(i+65),j*2+1,index,'DD', state)):
                                goodMoves.append([chr(i+65),j*2+1,index,'DD'])
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'DD'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'DD', state, player)):
                            if(isGood(chr(i+65),j*2+2,index,'DD', state)):
                                goodMoves.append([chr(i+65),j*2+2,index,'DD'])
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'DD'])
                    #####################################################
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'DL', state, player)):
                            if(isGood(chr(i+65),j*2+1,index,'DL', state)):
                                goodMoves.append([chr(i+65),j*2+1,index,'DL'])
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'DL'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'DL', state, player)):
                            if(isGood(chr(i+65),j*2+2,index,'DL', state)):
                                goodMoves.append([chr(i+65),j*2+2,index,'DL'])
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'DL'])

    return (badMoves, goodMoves)

def allBadMoves(state, player):
    badMoves = allPossibleMoves(state, player)[0]
    return badMoves

def allGoodMoves(state, player):
    goodMoves = allPossibleMoves(state, player)[1]
    return goodMoves

def showAllPossibleMoves(state, player):
    badMoves = allBadMoves(state, player)
    goodMoves = allGoodMoves(state, player)
    print(f"Losi potezi {current}:")
    for index, value in enumerate(badMoves):
        print(f"{index+1}.  [{value[0]}  {value[1]}  {value[2]}  {value[3]}]")
    print(f"Dobri potezi {current}:")
    for index, value in enumerate(goodMoves):
        print(f"{index+1}.  [{value[0]}  {value[1]}  {value[2]}  {value[3]}]")
          
                            
def showGameStateBasedOnPossibleMove(state, player):
    goodMoves = allGoodMoves(state, player)
    previousState = copy.deepcopy(state)
    for value in goodMoves:
        newState = play(state, value)
        table(newState)
        state = copy.deepcopy(previousState)

def minimaxBestMove(board):
    newBoard = copy.deepcopy(board)
    global current, computer
    bestScore = float('-inf')
    bestMove = None
    alpha = float('-inf')
    beta = float('inf')
    possibleMoves = allGoodMoves(board, current)  
    for index, move in enumerate(possibleMoves):
        resultState = play(newBoard, move)
        newBoard = copy.deepcopy(board)
        moveScore = minimax(resultState, 1, not computer, alpha, beta)
        if moveScore > bestScore:
            bestScore = moveScore
            bestMove = move
        alpha = max(alpha, moveScore)
        #print(f"best sc Beta {beta} and alpha {alpha} and Bestscore {bestScore}")
        #if(index == 1): break
    return bestMove
        

def minimax(state, depth, maxPlayer, alpha, beta):
    #print("minimax")
    if depth == 0 or endGame():
        val = evaluate(state)
        #print(f"Eval {val}")
        return val
    
    if maxPlayer:
        #print("maxPlayer minimax")
        return maxValue(state, depth, alpha, beta)
    else:
        #print("minPlayer minimax")
        return minValue(state, depth,  alpha, beta)

    
def maxValue(state, depth, alpha, beta):
    newState = copy.deepcopy(state)
    possibleMoves = allGoodMoves(state, current)
    maxValue = float('-inf')
    for move in possibleMoves:
        resultState = play(newState, move)
        newState = copy.deepcopy(state)
        score = minimax(resultState, depth-1, False, alpha, beta)
        maxValue = max(maxValue, score)
        alpha = max(alpha, score)
        #print(f"max val Beta {beta} and alpha {alpha} and score {score}")
        if beta <= alpha:
            break
    return maxValue


def minValue(state, depth, alpha, beta):
    newState = copy.deepcopy(state)
    possibleMoves = allGoodMoves(state, 'X' if current == 'O' else 'O')
    minValue = float('inf')
    for move in possibleMoves:
        resultState = play(newState, move)
        newState = copy.deepcopy(state)
        score = minimax(resultState, depth-1, True, alpha, beta)
        minValue = min(minValue, score)
        #print(f"min val Beta {beta} and alpha {alpha} and score {score}")
        beta = min(beta, score)
        if beta <= alpha:
            break
    return minValue


def evaluate(board):
    global current, n
    x=0
    o=0
    [x, o] = checkStack(board, x, o)
    #print(f"x:{x} o:{o}")
    #print(f"{current}")
    return x - o if current == 'X' else o - x

start()