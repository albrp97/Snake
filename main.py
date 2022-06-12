#Alberto Rodero for Damavis Challenge

import numpy as np
import time

# Evaluates weather a set of movements are valid for a snake in a board
# More efficient than evFunRecursive
def evaluationFunction(board, snake, movements):
    newSnake=np.array(snake)

    for m in movements:
        # Check board collision
        head = np.array(newSnake)[0]  # This makes a copy of original object so we are not modifying it
        if m == 'L':
            head[0] -= 1
            if head[0] < 0:
                return False #, "Board collision"
        elif m == 'U':
            head[1] -= 1
            if head[1] < 0:
                return False  # , "Board collision"
        elif m == 'R':
            head[0] += 1
            if head[0] >= board[0]:
                return False #, "Board collision"
        elif m == 'D':
            head[1] += 1
            if head[1] >= board[1]:
                return False #, "Board collision"

        # Delete latest snake cell
        # We do this before checking snake collision so the head can be were the tail used to
        s = np.array(newSnake[:-1])  # this also is making a copy of the original object

        # Check snake collision
        # Head is already modified with current movement when checking for board collision
        if np.any(np.all(head == s, axis=1)):
            return False #, "Snake collision"

        newSnake = []
        newSnake.append(head)
        for i in s:
            newSnake.append(i)
    return True

#Recursive call to get number and possible solutions
#Returns current number of solutions
def nOfPossibleSolutionsRecursive(board,snake,depth,currentSol,allSols,nEv):
    #Order of letters to check for solutions
    letters = "LURD"
    #Current number of solutions
    nSol=0
    #Checking all letters
    for letter in letters:
        checkSol=currentSol+letter
        nEv[0]+=1
        if evaluationFunction(board,snake,checkSol):   #for evaluation 2
            if depth==len(checkSol):
                #If the solution checks with depth then it is a final solution
                nSol+=1
                allSols.append(checkSol)
            else:
                #If it doesnt check it adds another letter in the next iteration
                nSol += nOfPossibleSolutionsRecursive(board,snake,depth,checkSol,allSols,nEv)
    return nSol

#Initial call to get solutions for a certain depth
#Return number of solutions and valid solutions
def nOfPossibleSolutions(board,snake,depth):
    allSols=[]
    nEv=[0] #Number of actual evaluations, in array so its a reference parameter
    if depth!=0:
        nSols=nOfPossibleSolutionsRecursive(board,snake,depth,"",allSols,nEv)
    else:
        nSols=0
    return nSols,allSols,nEv

#Dimensions of the board [x,y]
board = [4, 3]
#Cells the snake is occupying, first element is head, latest is tail
snake =  [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
#Depth of movements the algorithm is going to look for a solution
depth = 8

t=time.time()
finalSol=nOfPossibleSolutions(board,snake,depth)
t=time.time()-t


print("Parameters\nDepth: "+depth.__str__()+"\tBoard: "+board.__str__()+"\tSnake: "+snake.__str__())
print("\nNumber of solutions: "+finalSol[0].__str__())
print("\nAll solutions: "+finalSol[1].__str__())
print("\nNumber of possible combinations: "+pow(4,depth).__str__()+"\nNumber of total evaluations: "+finalSol[2][0].__str__())
print("We are evaluating "+round((finalSol[2][0]*100/pow(4,depth)),2).__str__()+"% of all possible evaluations")
print("\nExecution time: "+t.__str__()+" seconds")

