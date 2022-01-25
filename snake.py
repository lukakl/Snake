def game():
    # 7x7 playing field
    rows, cols = (7,7)
    field = [[0 for i in range(cols)] for j in range(rows)]
    field[3][3] = 9
    for row in field:
        print(row)
    

game()