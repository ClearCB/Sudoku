from src.checkEsCuadrado import esCuadrado
import pytest

@pytest.mark.esCuadradoUno
def testEsCuadradoUno():
    assert esCuadrado([[1,2,3],
                       [2,3,1]]) == False

@pytest.mark.esCuadradoDos
def testEsCuadradoDos():
    assert esCuadrado([[1,2,3],
                       [2,3,1],
                       [3,1]]) == False

@pytest.mark.esCuadradoTres
def testEsCuadradoTres():
    assert esCuadrado([[1,2,3],
                       [2,3,1],
                       [3,1,2]]) == True
