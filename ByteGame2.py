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

def table():
    global n
    global matrix
    global resultX
    global resultO
    header(n)
    #matrix[2][0]=['1','2','3','4','5', '6','7','8']
    #matrix[2][2]=['X','X','O','O','X']
    #matrix[7][3]=['O','X','X','O','X']
    #matrix[7][2]=['X','O','X','X','X']
    for x in range(0,n):
        if (x%2==0):
            row=9
            while(row>0):
                if(row==6):
                    print(string.ascii_uppercase[x], end=' ') #/////////////
                else:
                    print('  ', end='') #////////////////////////
                for y in range(0,int(n/2)):                      
                    if (len(matrix[x][y])==0):
                        print('. . .', end='   ') #crno
                        print('   ',end='   ') #belo
                    else:
                        if (len(matrix[x][y])>row-3 and len(matrix[x][y])<=row):
                            for el in range(row-3, len(matrix[x][y])):
                                print(f'{matrix[x][y][el]}', end=' ')
                            for el in range(len(matrix[x][y]),row):
                                print('.', end=' ')
                            #print('6 . .', end='   ') #crno
                            print('',end='  ')
                            print('   ',end='   ') #belo
                        elif (len(matrix[x][y])>row):
                            for el in range(row-3, row):
                                print(f'{matrix[x][y][el]}', end=' ')
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
                    if (len(matrix[x][y])==0):
                        print('   ',end='   ')
                        print('. . .', end='   ') #crno
                        #print('   ',end='   ') #belo
                    else:
                        if (len(matrix[x][y])>row-3 and len(matrix[x][y])<=row):
                            print('   ',end='   ')
                            for el in range(row-3, len(matrix[x][y])):
                                print(f'{matrix[x][y][el]}', end=' ')
                            for el in range(len(matrix[x][y]),row):
                                print('.', end=' ')
                            #print('   ',end='   ')
                            #print('. . .', end='   ') #crno
                            print('',end='  ')
                            #print('   ',end='   ') #belo
                        elif (len(matrix[x][y])>row):
                            print('   ',end='   ')
                            for el in range(row-3, row):
                                print(f'{matrix[x][y][el]}', end=' ')
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
    global current

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
        print ("Polje ne postoji na tabli")
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
        print('Polje je prazno.')
        return False    
    return True
    
def checkFigureAtIndex(i, j, index):
    row = ord(i)-65
    column = j - 1

    #matrix[row][column] = ['x', 'O', 'O']
    #print(matrix[row])
    #print(matrix[row][column])
    #print(len(matrix[row][column]))
    #print(matrix[row][column][el])
    square = matrix[row][int(column/2)]
    if (len(square) <= index):
        print("Mesto u polju koje ste zadali je prazno.")
        return False   
    return True
    
def checkDirection(dir):
    global direction
    correctDir = False
    for d in direction:
        if (dir == d):
            correctDir = True
            #print("Uneli ste validnu vrednost za smer.")
    if (correctDir == False):
        print("Uneli ste nevalidnu vrednost za smer.")
    return correctDir

#funkcija koja proverava da li je polje gore levo prazno
def checkAdjacentUpperLeftField(i, j):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True

    if (row > 0 and column > 0):      
        if (row % 2 != 0):
            goreLevo = matrix[row - 1][int(column/2)] 
        else:
            goreLevo = matrix[row - 1][int((column - 1)/2)]  
        if len(goreLevo) != 0:     
            #print(f"Polje gore levo [{i}][{j}] nije prazno polje.")
            prazno = False 
    return prazno

#funkcija koja proverava da li je polje gore desno prazno
def checkAdjacentUpperRigtField(i, j):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True
 
    if (row > 0 and column < n - 1):      
        if (row % 2 != 0):
            goreDesno = matrix[row - 1][int((column + 1)/2)] 
        else:
            goreDesno = matrix[row - 1][int(column/2)]  
        if len(goreDesno) != 0:     
            #print(f"Polje gore desno [{i}][{j}] nije prazno polje.")
            prazno = False  
    return prazno

# funkcija koja proverava da li je polje dole desno prazno
def checkAdjacentLowerRightField(i, j):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True

    if (row < n - 1 and column < n - 1): 
        if(row % 2 != 0):
            doleDesno = matrix[row + 1][int((column + 1)/2)]  
        else:
            doleDesno = matrix[row + 1][int(column/2)]
        if len(doleDesno) != 0:
            #print(f"Polje dole desno [{i}][{j}] nije prazno polje.")
            prazno = False  
    return prazno

# funkcija koja proverava da li je polje dole levo prazno
def checkAdjacentLowerLeftField(i, j):
    row = ord(i) - 65
    column = j - 1
 
    prazno = True

    if (row < n - 1 and column > 0): 
        if(row % 2 != 0):
            doleLevo = matrix[row + 1][int(column/2)]  
        else:
            doleLevo = matrix[row + 1][int((column - 1)/2)]
        if len(doleLevo) != 0:
            #print(f"Polje dole levo [{i}][{j}] nije prazno polje.")
            prazno = False 

    return prazno

def newPostionOfFigure(i, j, dir):
    
    global n, matrix
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

def checkAdjacentFields(i, j, dir):
        valid = False
        if (dir == "GL" and (checkAdjacentUpperLeftField(i, j) == False)):
            valid = True
        if (dir == "GD" and (checkAdjacentUpperRigtField(i, j) == False)):
            valid = True
        if (dir == "DL" and (checkAdjacentLowerLeftField(i, j) == False)):
            valid = True
        if (dir == "DD" and (checkAdjacentLowerRightField(i, j) == False)):
            valid = True
    
        if(checkAdjacentLowerRightField(i, j) and checkAdjacentLowerLeftField(i, j) and checkAdjacentUpperRigtField(i, j) and checkAdjacentUpperLeftField(i, j)):
            valid = True
        return valid

def checkIfLeadsToClosestStack(i, j, dir):
    global n, matrix
    row = ord(i) - 65
    column = j - 1
    nextStep = newPostionOfFigure(i, j, dir)
    

    currStep = (row, int(column/2))
    #print("Curent pos " + str(currStep))
    #print("Next pos " + str(nextStep))
    

    for ind1 in range(0,n):
        for ind2 in range(0,int(n/2)):
            if(len(matrix[ind1][ind2])!=0 and ind1 != currStep[0] and ind2 != currStep[1]):
                stack = (ind1, ind2)
                newDistance = distance(stack, nextStep)
                currDistance = distance(stack, currStep)
                # print(f"Curr {currDistance} {stack[0]},{stack[1]*2} {currStep[0]},{currStep[1]*2}")
                # print(f"New {newDistance} {stack[0]},{stack[1]*2} {nextStep[0]},{nextStep[1]*2}")
                if (newDistance < currDistance):
                    return True
                
    return False

def distance(pos1, pos2):
    # Manhattan distance |x1-x2|+|y1-y2|
    return abs(pos1[0] - pos2[0]) + abs(pos1[1]*2 - pos2[1]*2)

def checkHeightOfStacks(i, j, index ,dir):
    global n, matrix
    row = ord(i) - 65
    column = j - 1

    position = newPostionOfFigure(i,j,dir)
    nextStep = matrix[position[0]][position[1]]
    #print(nextStep)
    nextStepHeight = len(nextStep)
    if (nextStepHeight <= index):
        #print("Novi idex "+str(nextStepHeight)+" stari "+str(index))
        return False
    #print("Novi idex "+str(nextStepHeight)+" stari "+str(index))
    return True

def isGood(i, j, index, dir):
    global current, matrix, n
    row = ord(i)-65
    column = j - 1

    if(checkAdjacentFields(i, j, dir)):
        if(checkIfLeadsToClosestStack(i, j, dir)):
            if(checkHeightOfStacks(i, j, index, dir)):
                return True
    return False
    
def isValid(i, j, index, dir):

    global current, matrix, n
    row = ord(i)-65
    column = j - 1
    #dodatak
    if(row % 2 == 0 and column % 2 != 0):
        return False
    if(row % 2 !=0 and column % 2 == 0):
        return False
    if(matrix[row][int(column/2)][index] != current):
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

def play(i,j,index, dir):
    global matrix
    global current
    row= ord(i) - 65
    column=j-1

    
    element = list()
    for x in range(index, len(matrix[row][int(column/2)])):
        element.append(matrix[row][int(column/2)][x])
    #print(element)
    #print(matrix[row][int(column/2)])
    
    if(dir == 'DD'):
        for x in range(0, len(element)):
            if(column % 2 == 0):
                matrix[row+1][int(column/2)].append(element[x])
            else:
                matrix[row+1][int(column/2)+1].append(element[x])
    elif(dir == 'GD'):
        for x in range(0, len(element)):
            if(column % 2 == 0):
                matrix[row-1][int(column/2)].append(element[x])
            else:
                matrix[row-1][int(column/2)+1].append(element[x])
    elif(dir == 'GL'):
        for x in range(0, len(element)):
            if(column % 2 == 0):
                matrix[row-1][int(column/2)-1].append(element[x])
            else:
                matrix[row-1][int(column/2)].append(element[x])
    else:
        for x in range(0, len(element)):
            if(column % 2 == 0):
                matrix[row+1][int(column/2)-1].append(element[x])
            else:
                matrix[row+1][int(column/2)].append(element[x])

    for x in element:
        matrix[row][int(column/2)].remove(x)

    checkStack()

def checkStack():
    global matrix
    global n
    global resultX
    global resultO
    global current

    for i in range(0,n):
        for j in range(0,int(n/2)):
            if(len(matrix[i][j]) == 8):
                if(matrix[i][j][7] == 'X'):
                    #print("Hey X")
                    resultX+=1
                    matrix[i][j].clear()
                else:
                    #print("Hey O")
                    resultO+=1
                    #print(matrix[i][j])
                    matrix[i][j].clear()


def endGame():
    global resultX
    global resultO
    global winner
    global n

    stackNum = n/8
    if(resultX>int(stackNum/2)):
        winner = 'X'
        return True 
    elif(resultO>int(stackNum/2)):
        winner = 'O'
        return True
    else: 
        return False

def start():

    global current

    # init()
    # table()
    # for i in range(0, n): 
    #     for j in range(0, int(n/2)):
    #         matrix[i][j] = []
    # table()
    # #matrix[1][0] = ['X','O','O']
    # #matrix[4][3] = ['X','O','X','X']
    # matrix[1][0] = ['X','O','O']
    # matrix[2][1] = ['X','O','X','X']
    # table()

    # print(checkHeightOfStacks('C', int(3), int(4), 'GL'))

    #print(checkIfLeadsToClosestStack('B', int(2), 'DL'))

    isFirstToPlay()
    if (init()):
        #matrix[5][1] = ['X','O','O','O','X','O','X','X']
        table()
        while(True):

            if(endGame()):
                print("Kraj igre! Pobednik je: " + winner)
                break
            
            showAllPossibleMoves()
            showGameStateBasedOnPossibleMove()
            i = input("Unesite vrstu polja na kom se figura nalazi: ")
            j = input("Unesite kolonu polja na kom se figura nalazi: ")
            index = input("Unesite indeks figure u polju: ")
            dir = input("Unesite smer u kom zelite da pomerite figuru: ")
            #print(f"{i}{j}{index}{dir}")
            if(isValid(i,int(j),int(index), dir)):
                play(i,int(j),int(index),dir)
                table()
                if(current == 'X'):
                    current = 'O'
                else:
                    current ='X'
                print("Na potezu je: " + current)
            else:
                print("Niste uneli validan potez!")
    else:
        return False

def allPossibleMoves():
    global n, matrix, current
    #matrix[1][0] = ['X','X','O']
    goodMoves = []
    badMoves = []
    for i in range(0,n):
        for j in range(0,int(n/2)):
            for index, value in enumerate(matrix[i][j]):      
                if(value == current):
                    #print(value)
                    #print("Polje "+str(chr(i+65))+" "+str(j*2+2)+" "+str(isValid(chr(i+65),j*2+2,index,'GL')))
                    #print(matrix[i][j])
                    #print(f"Index: {index}, Value: {value}")
                    
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'GL')):
                            if(isGood(chr(i+65),j*2+1,index,'GL')):
                                goodMoves.append([chr(i+65),j*2+1,index,'GL'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+1} {index} GL]")
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'GL'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'GL')):
                            if(isGood(chr(i+65),j*2+2,index,'GL')):
                                goodMoves.append([chr(i+65),j*2+2,index,'GL'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+2} {index} GL]")
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'GL'])
                    #######################################################
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'GD')):
                            if(isGood(chr(i+65),j*2+1,index,'GD')):
                                goodMoves.append([chr(i+65),j*2+1,index,'GD'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+1} {index} GD]")
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'GD'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'GD')):
                            if(isGood(chr(i+65),j*2+2,index,'GD')):
                                goodMoves.append([chr(i+65),j*2+2,index,'GD'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+2} {index} GD]")
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'GD'])
                    ####################################################
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'DD')):
                            if(isGood(chr(i+65),j*2+1,index,'DD')):
                                goodMoves.append([chr(i+65),j*2+1,index,'DD'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+1} {index} DD]")
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'DD'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'DD')):
                            if(isGood(chr(i+65),j*2+2,index,'DD')):
                                goodMoves.append([chr(i+65),j*2+2,index,'DD'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+2} {index} DD]")
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'DD'])
                    #####################################################
                    if(i % 2 == 0):
                        if(isValid(chr(i+65),j*2+1,index,'DL')):
                            if(isGood(chr(i+65),j*2+1,index,'DL')):
                                goodMoves.append([chr(i+65),j*2+1,index,'DL'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+1} {index} DL]")
                            else:
                                badMoves.append([chr(i+65),j*2+1,index,'DL'])
                    else:
                        if(isValid(chr(i+65),j*2+2,index,'DL')):
                            if(isGood(chr(i+65),j*2+2,index,'DL')):
                                goodMoves.append([chr(i+65),j*2+2,index,'DL'])
                                #print(f"{x}.  [{chr(i+65)} {j*2+2} {index} DL]")
                            else:
                                badMoves.append([chr(i+65),j*2+2,index,'DL'])

    return (badMoves, goodMoves)

def showAllPossibleMoves():
    moves = allPossibleMoves()
    print(f"Losi potezi {current}:")
    for index, value in enumerate(moves[0]):
        print(f"{index+1}.  [{value[0]}  {value[1]}  {value[2]}  {value[3]}]")
    print(f"Dobri potezi {current}:")
    for index, value in enumerate(moves[1]):
        print(f"{index+1}.  [{value[0]}  {value[1]}  {value[2]}  {value[3]}]")
    
                            
def showGameStateBasedOnPossibleMove():
    goodMoves = allPossibleMoves()[1]
    global matrix, n
    previousState = copy.deepcopy(matrix)
    #print(previousState)
    for value in goodMoves:
        play(value[0],value[1],value[2],value[3])
        table()
        for i in range(0,n):
            for j in range(0,int(n/2)):
                matrix[i][j] = previousState[i][j]
        previousState = copy.deepcopy(matrix)
        #table()
    #############################
    # play('C', 1, 0, "DD")
    # print(previousState)
    # table()
    # for i in range(0,n):
    #     for j in range(0,int(n/2)):
    #         matrix[i][j] = previousState[i][j]
    # table()
    # previousState = copy.deepcopy(matrix)
    # play('C', 1, 0, "GD")
    # print(previousState)
    # table()
    # for i in range(0,n):
    #     for j in range(0,int(n/2)):
    #         matrix[i][j] = previousState[i][j]
    # table()

start()