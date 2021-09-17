#  ________            _   __                                                              ___   ____ ___  ___
# /_  __/ /_  ___     / | / /__  __  ___________  ____ ___  ____ _____  ________  _____   |__ \ / __ \__ \<  /
#  / / / __ \/ _ \   /  |/ / _ \/ / / / ___/ __ \/ __ `__ \/ __ `/ __ \/ ___/ _ \/ ___/   __/ // / / /_/ // / 
# / / / / / /  __/  / /|  /  __/ /_/ / /  / /_/ / / / / / / /_/ / / / / /__/  __/ /      / __// /_/ / __// /  
#/_/ /_/ /_/\___/  /_/ |_/\___/\__,_/_/   \____/_/ /_/ /_/\__,_/_/ /_/\___/\___/_/      /____/\____/____/_/   

# First Law
#    A robot may not injure a human being or, through inaction, allow a human being to come to harm.
# Second Law
#    A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
# Third Law
#    A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.                                                                                                            


# I was listening to Goldfinger-Spokesman on my Arch system while making this ;)

def printMatrix(matrix):
    for i in range(9):
        for j in range(9):
            print(str(matrix[i][j]),end=" ")
        print()

# I use Arch btw...

def findFirstEmpty(matrix, l):
    for i in range(9):
        for j in range(9):
            if(matrix[i][j]== 0):
                l[0]= i
                l[1]= j
                return True
    return False

# Did I mention I use Arch ?


#Ovo su samo osnovne pripremne funkcije za celu jebadu...
def isInRow(matrix,row,element):
    for j in range(9):
        if(matrix[row][j] == element):
            return True
    return False

def isInColumn(matrix,col,element):
    for j in range(9):
        if(matrix[j][col] == element):
            return True
    return False

def isInBox(matrix,row,col,element):
    for i in range(3):
        for j in range(3):
            if(matrix[i + row][j + col] == element):
                return True
    return False

#Spojili se kao mocni rendzeri.
def isSafe(matrix,row,col,element):
    return not isInRow(matrix,row,element) and not isInColumn(matrix,col,element) and not isInBox(matrix,row - row % 3, col - col % 3,element)
        
        


#Ovo je jebada pomenuta gore
def solveBoard(matrix):
    el = [0,0]
    
    #provera da li je popunjena vec
    if(not findFirstEmpty(matrix,el)):
        return True

    row = el[0]
    col = el[1]

    for i in range(1,10):
        
        if(isSafe(matrix,row,col,i)):
            matrix[row][col] = i
            
            #Ovo je srce rekurzije , tj. glava mocnog rendzera
            if(solveBoard(matrix)):
                return True
            
            matrix[row][col] = 0
    return False

# Srbija do Tokija !
