def checkRegionTresTres (sudoku):

    correcto = []
    for num in range(1,len(sudoku)+1):
        correcto.append(num)

    correcto = sorted(correcto)
        
    for linea in range(3):
        for columna in range(3):
            region = []
            for line in sudoku[linea*3:(linea+1)*3]:
                region += line[columna*3:(columna+1)*3]

            if sorted(region) == correcto:
                continue
            else:
                return False


if __name__ == "__main__":

    assert checkRegionTresTres([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                [9, 1, 2, 3, 4, 5, 6, 7, 8]]) == False
