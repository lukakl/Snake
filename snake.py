import os
from random import randint
import time

def game():

    rows, cols = (7, 7)

    #creates 2d array
    grid = [[0 for i in range(rows)] for j in range(cols)]

    #creates 1000ms game tick using while loop
    a = 0
    while a <= 0:
        
        os.system("cls")

        x = randint(0, 6)
        y = randint(0, 6)
        food = randint(1, 100)

        #adds 1/3 chance of spawning food
        if food < 34:
                grid[x][y] = 1

        for f in grid:
            print(f)

        time.sleep(1)
    
game()