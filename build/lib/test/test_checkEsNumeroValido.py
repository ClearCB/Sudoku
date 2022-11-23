from src.checkEsNumeroValido import esValido
import pytest


@pytest.mark.esValidoUno
def testValidoUno():

    assert esValido([  [1,2,3],
                       [2,3,1],
                       [3,1]]) == True
    
@pytest.mark.esValidoDos
def testValidoDos():

    assert esValido([  [1,2,3],
                       [24634,3,1],
                       [3,1]]) == False

@pytest.mark.esValidoTres
def testValidoTres():

    assert esValido([  [1,2,3],
                       [2,3,1],
                       [3,-1]]) == False
