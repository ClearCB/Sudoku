from src.compararLineas import compararLineas
import pytest


@pytest.mark.compararLineasUno
def testValidoUno():

    assert compararLineas([[1,2,3],[1,2,3]]) == True

    
@pytest.mark.compararLineasDos
def testValidoDos():

    assert compararLineas([[1,2,3],
                       [3,1]]) == True

@pytest.mark.compararLineasTres
def testValidoTres():

    assert compararLineas([[1,2,2],
                       [2,3,1],
                       [3,-1]]) == False

@pytest.mark.compararLineasCuatro
def testValidoTres():

    assert compararLineas([[1,2,2],
                       [2,3,1],
                       [3,-1]]) == False

@pytest.mark.compararLineasCinco
def testValidoTres():

    assert compararLineas([[1,2,3],
                       [2,3,1],
                       [3,3,1]]) == False
