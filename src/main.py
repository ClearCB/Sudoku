from src.checkEsCuadrado import esCuadrado
from src.checkEsNumeroValido import esValido
from src.compararColumnas import compararColumnas
from src.compararLineas import compararLineas
from src.checkRegionTresTres import checkRegionTresTres

def sudokuValidator(sudoku):

    siEsCuadrado = esCuadrado(sudoku)
    siEsValido = esValido(sudoku)
    noRepiteColumnas = compararColumnas(sudoku)
    noRepiteFila = compararLineas(sudoku)

    if len(sudoku) == 9:
        checkRegionTresTres(sudoku)
        if checkRegionTresTres and siEsCuadrado and siEsValido and noRepiteColumnas and noRepiteFila:
            return True
    
    elif siEsCuadrado and siEsValido and noRepiteColumnas and noRepiteFila:
        return True
    else:
        return False

if __name__ == "__main__":

    from checkEsCuadrado import esCuadrado
    from checkEsNumeroValido import esValido
    from compararColumnas import compararColumnas
    from compararLineas import compararLineas
    from checkRegionTresTres import checkRegionTresTres



    assert sudokuValidator([[1,2,3,4],
                            [2,3,1,3],
                            [3,1,2,3],
                            [4,4,4,2]]) == False
    
    assert sudokuValidator([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [2, 3, 4, 5, 6, 7, 8, 9, 1],
                            [3, 4, 5, 6, 7, 8, 9, 1, 2],
                            [4, 5, 6, 7, 8, 9, 1, 2, 3],
                            [5, 6, 7, 8, 9, 1, 2, 3, 4],
                            [6, 7, 8, 9, 1, 2, 3, 4, 5],
                            [7, 8, 9, 1, 2, 3, 4, 5, 6],
                            [8, 9, 1, 2, 3, 4, 5, 6, 7],
                            [9, 1, 2, 3, 4, 5, 6, 7, 8]]) == False


