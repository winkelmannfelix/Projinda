directions = {
    'up': (0, 1),
    'down': (0, -1),
    'left': (-1, 0),
    'right': (1, 0)
}

def changeDirection(currentDirection, input): #snakes current direction and keyboard input
    newDirection = input        
    if currentDirection != newDirection:
        if (currentDirection[0] + newDirection[0], currentDirection[1] + newDirection[1]) != (0, 0):    #So that you cant make a 180 turn
            return newDirection
    else:
        return currentDirection # if input is same as current direction, don't change direction