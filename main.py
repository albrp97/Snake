#Alberto Rodero for Damavis Challenge

import numpy as np

# Evaluates weather a set of movements are valid for a snake in a board
def evaluationFunction(board, snake, depth, movements):
    # Since depth is always len(movements), n of parameters could be shortened
    # for it makes no sense to hace depth>movements or viceversa

    # For ONE movement
    m = movements[0]

    # Check board collision
    head = np.array(snake)[0]  # This makes a copy of original object so we are not modifying it
    # todo switch for a switch to check efficiency
    if m == 'L':
        head[0] -= 1
        if head[0] < 0:
            return False #, "Board collision"
    elif m == 'R':
        head[0] += 1
        if head[0] >= board[0]:
            return False #, "Board collision"
    elif m == 'U':
        head[1] -= 1
        if head[1] < 0:
            return False #, "Board collision"
    elif m == 'D':
        head[1] += 1
        if head[1] >= board[1]:
            return False #, "Board collision"

    # Delete latest snake cell
    s = np.array(snake[:-1])  # this also is making a copy of the original object

    # Check snake collision
    # Head is already modified with current movement when checking for board collision
    if np.any(np.all(head == s, axis=1)):
        return False #, "Snake collision"

    newSnake = []
    newSnake.append(head)
    for i in s:
        newSnake.append(i)

    # If depth is 1 return true
    if depth == 1:
        return True
    # Otherwise recursive call
    else:
        return evaluationFunction(board, newSnake, depth - 1, movements[1:])

#Recursive call to get number and possible solutions
#Returns current number of solutions
def nOfPossibleSolutionsRecursive(board,snake,depth,currentSol,allSols):
    #Order of letters to check for solutions
    letters = "LURD"
    #Current number of solutions
    nSol=0
    #Checking all letters
    for i in range(4):
        checkSol=currentSol+letters[i]
        if evaluationFunction(board,snake,len(checkSol),checkSol):
            if depth==len(checkSol):
                #If the solution checks with depth then it is a final solution
                nSol+=1
                allSols.append(checkSol)
            else:
                #If it doesnt check it adds another letter in the next iteration
                nSol += nOfPossibleSolutionsRecursive(board,snake,depth,checkSol,allSols)
    return nSol

#Initial call to get solutions for a certain depth
#Return number of solutions and valid solutions
def nOfPossibleSolutions(board,snake,depth):
    allSols=[]
    nSols=nOfPossibleSolutionsRecursive(board,snake,depth,"",allSols)
    return nSols,allSols

#Dimensions of the board [x,y]
board = [2, 3]
#Cells the snake is occupying, first element is head, latest is tail
snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
#Depth of movements the algorithm is going to look for a solution
depth = 10

finalSol=nOfPossibleSolutions(board,snake,depth)
print("Parameters\nDepth: "+depth.__str__()+"\tBoard: "+board.__str__()+"\tSnake: "+snake.__str__())
print("\nNumber of solutions: "+finalSol[0].__str__())
print("\nAll solutions: "+finalSol[1].__str__())

