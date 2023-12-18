import sys
import string

current = 'X'
firstPlayer = 0
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
        #for x in matrix:
            #print(x)
    #print('---------------------------------------')
    #pocetno stanje matrice
    for i in range(0, n): 
        for j in range(0, int(n/2)): 
            if (i != 0 and i != n-1): 
                if (i % 2 == 0):
                    matrix[i][j].append('O')
                else:
                    matrix[i][j].append('X')
    #for x in matrix:
            #print(x)
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

    global firstPlayer
    global current

    print("Ko igra prvi? (0-covek, 1-racunar):")
    firstPlayer = int(sys.stdin.readline())
    if(firstPlayer==0):
        print("Covek je prvi na potezu.")
    else:
        print("Racunar je prvi na potezu.")

    print("Da li zelite da budete X ili O?")
    current = sys.stdin.readline()

def checkIfFieldExists (i, j):
    row = ord(i) - 65
    column = j - 1
    if (row >= n and column >= n):
        print ("Polje ne postoji na tabli")
        return False
 
def checkIfFieldIsFilled(i, j):
    row = ord(i) - 65
    column = j - 1
    isFilled = False 
    for x in matrix[row][column]:
        if(x == 'X' or x == 'O'):
            isFilled = True
    if(isFilled == False):
        print('Polje je prazno.')
        return False
    
def checkFigureAtIndex(i, j, index):
    row = ord(i)-65
    column = j - 1

    #matrix[row][column] = ['x', 'O', 'O']
    #print(matrix[row])
    #print(matrix[row][column])
    #print(len(matrix[row][column]))
    #print(matrix[row][column][el])
    square = matrix[row][column]
    if (len(square) <= index):
        print("Mesto u polju koje ste zadali je prazno.")
        return False
    
def checkDirection(dir):
    global direction
    correctDir = False
    for d in direction:
        if (dir == d):
            correctDir = True
    if (correctDir == False):
        print("Uneli ste nevalidnu vrednost za smer.")
        return False
    
def isValid(i, j, index, dir):

    #proveriti da li zadato polje postoji na tabli
    checkIfFieldExists(i, j)
    #proveriti da li postoje figure na zadatom polju
    checkIfFieldIsFilled(i, j)
    #proveriti da li postoji figura na zadatom mestu na steku na zadatom polju  
    checkFigureAtIndex(i, j, index)
    
    #proveriti da li je smer jedan od cetiri moguca
    checkDirection(dir)
    
    return True

def start():

    #isFirstToPlay()
    if (init()):
        table()
        #print(isValid('B',7, 0, 'DD'))
    else:
        return False

    

start()