def compararColumnas(sudoku):

    indice = 0
    columnas = len(sudoku)

    while indice != columnas:

        columna = []
        for linea in sudoku:
            
            columna.append(linea[indice])
        
        for numero in columna:

            cuentaNumero = columna.count(numero)

            if cuentaNumero > 1:
                return False
        
        indice += 1

    return True

if __name__ == "__main__":

    assert compararColumnas([[1,2,3],
                             [2,2,1]]) == False

    assert compararColumnas([[1,2,3],
                             [3,1,2]]) == True

    assert compararColumnas([[1,2,2],
                             [2,3,1],
                             [3,-1,4]]) == True

    assert compararColumnas([[1,2,3],
                             [2,3,1],
                             [3,1,2]]) == True

    assert compararColumnas([[1,2,3],
                             [2,3,1],
                             [3,3,1]]) == False
