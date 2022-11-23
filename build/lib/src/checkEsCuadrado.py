def esCuadrado(sudoku):

    assert isinstance(sudoku, list)

    numerosColumna = len(sudoku)

    for columnas in sudoku:

        numerosFila = len(columnas)

        if numerosFila == numerosColumna:
            continue
        else:
            return False
        
    return True


if __name__ == "__main__":

    assert esCuadrado([[1,2,3],
                       [2,3,1]]) == False
    
    assert esCuadrado([[1,2,3],
                       [2,3,1],
                       [3,1]]) == False
