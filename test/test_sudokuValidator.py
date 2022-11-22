from src.main import sudokuValidator
import pytest

@pytest.mark.sudokuValidatorUno
def testSudokuValidatorUno():
    
    assert sudokuValidator([[1,2,3],
                            [2,3,1],
                            [3,1,2]]) == True
    
@pytest.mark.sudokuValidatorDos
def testSudokuValidatorDos():
    
    assert sudokuValidator([[1,2,3,4],
                            [2,3,1,3],
                            [3,1,2,3],
                            [4,4,4,2]]) == False
    
@pytest.mark.sudokuValidatorTres
def testSudokuValidatorTres():
    
    assert sudokuValidator([[1,2,3,4,5],
                            [2,3,1,5,6],
                            [4,5,2,1,3],
                            [3,4,5,2,1],
                            [5,6,4,3,2]]) == False
    