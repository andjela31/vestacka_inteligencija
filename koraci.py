def table2():
    global n
    global matrix
    header(n)
    matrix[2][0]=['1','2','3','4','5', '6','7','8']
    matrix[2][2]=[]
    for x in range(0,n):
        if (x%2==0):

            print('  ', end='') #////////////////////////
            for y in range(0,int(n/2)):                      
                if (len(matrix[x][y])==0):
                    print('. . .', end='   ') #crno
                    print('   ',end='   ') #belo
                else:
                    if (len(matrix[x][y])>6):
                        for el in range(6, len(matrix[x][y])):
                            print(f'{matrix[x][y][el]}', end=' ')
                        for el in range(len(matrix[x][y]),9):
                            print('.', end=' ')
                        #print('6 . .', end='   ') #crno
                        print('',end='  ')
                        print('   ',end='   ') #belo
                    else:
                        print('. . .', end='   ') #crno
                        print('   ',end='   ') #belo
            print('')

            print(string.ascii_uppercase[x], end=' ') #/////////////
            for y in range(0,int(n/2)):                      
                if (len(matrix[x][y])==0):
                    print('. . .', end='   ') #crno
                    print('   ',end='   ') #belo
                else:
                    if (len(matrix[x][y])>3 and len(matrix[x][y])<=6):
                        for el in range(3, len(matrix[x][y])):
                            print(f'{matrix[x][y][el]}', end=' ')
                        for el in range(len(matrix[x][y]),6):
                            print('.', end=' ')
                        #print('6 . .', end='   ') #crno
                        print('',end='  ')
                        print('   ',end='   ') #belo
                    elif (len(matrix[x][y])>6):
                        for el in range(3, 6):
                            print(f'{matrix[x][y][el]}', end=' ')
                        #print('6 . .', end='   ') #crno
                        print('',end='  ')
                        print('   ',end='   ') #belo
                    else:
                        print('. . .', end='   ') #crno
                        print('   ',end='   ') #belo
            print('')

            print('  ', end='') #////////////////////////
            for y in range(0,int(n/2)):                      
                if (len(matrix[x][y])==0):
                    print('. . .', end='   ') #crno
                    print('   ',end='   ') #belo
                else:
                    if (len(matrix[x][y])>0 and len(matrix[x][y])<=3):
                        for el in range(0, len(matrix[x][y])):
                            print(f'{matrix[x][y][el]}', end=' ')
                        for el in range(len(matrix[x][y]),3):
                            print('.', end=' ')
                        #print('6 . .', end='   ') #crno
                        print('',end='  ')
                        print('   ',end='   ') #belo
                    elif (len(matrix[x][y])>3):
                        for el in range(0, 3):
                            print(f'{matrix[x][y][el]}', end=' ')
                        #print('6 . .', end='   ') #crno
                        print('',end='  ')
                        print('   ',end='   ') #belo
                    else:
                        print('. . .', end='   ') #crno
                        print('   ',end='   ') #belo
            print('')


        else:
            k=0
            while(k<3):
                if(k%2==0):
                    print('  ', end='') #////////////////////////
                else:
                    print(string.ascii_uppercase[x], end=' ') #/////////////
                for y in range(0,int(n/2)):                      
                    if (len(matrix[x][y])==0):
                        print('   ',end='   ')
                        print('. . .', end='   ') #crno
                        #print('   ',end='   ') #belo
                #print('')

                for y in range(0,int(n/2)):                      
                    if (len(matrix[x][y])>0):
                        print('   ',end='   ')
                        print('. . .', end='   ') #crno
                        #print('   ',end='   ') #belo
                print('')

                k+=1