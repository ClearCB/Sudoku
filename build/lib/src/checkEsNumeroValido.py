def esValido(sudoku):

    numerosValidos = []
    
    for i in range(1,len(sudoku)+1):
        numerosValidos.append(i)

    for fila in sudoku:

        for numero in fila:

            if numero in numerosValidos:
                continue
            else:
                return False

    return True