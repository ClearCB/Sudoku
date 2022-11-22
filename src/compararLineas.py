def compararLineas(sudoku):

    for linea in sudoku:

        for numero in linea:

            cuentaNumero = linea.count(numero)

            if cuentaNumero > 1:
                return False
                
    return True