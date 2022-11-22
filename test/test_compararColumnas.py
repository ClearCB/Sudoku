from src.compararColumnas import compararColumnas
import pytest


@pytest.mark.compararColumnasUno
def testValidoUno():

    assert compararColumnas([[1,2,3],
                             [2,2,1]]) == False

    
@pytest.mark.compararColumnasDos
def testValidoDos():

    assert compararColumnas([[1,2,3],
                             [3,1,2]]) == True

@pytest.mark.compararColumnasTres
def testValidoTres():

    assert compararColumnas([[1,2,2],
                             [2,3,1],
                             [3,-1,4]]) == True

@pytest.mark.compararColumnasCuatro
def testValidoTres():

    assert compararColumnas([[1,2,3],
                             [2,3,1],
                             [3,1,2]]) == True

@pytest.mark.compararColumnasCinco
def testValidoTres():

    assert compararColumnas([[1,2,3],
                             [2,3,1],
                             [3,3,1]]) == False