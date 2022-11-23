from src.checkRegionTresTres import checkRegionTresTres
import pytest


@pytest.mark.checkRegionUno
def testRegionUno():

    assert checkRegionTresTres([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                [9, 1, 2, 3, 4, 5, 6, 7, 8]]) == False

# @pytest.mark.checkRegionDos
# def testRegionDos():

#     assert checkRegionTresTres([[1,2,3],
#                        [24634,3,1],
#                        [3,1]]) == False

# @pytest.mark.checkRegionTres
# def testRegionTres():

#     assert checkRegionTresTres([[1,2,3],
#                        [2,3,1],
#                        [3,-1]]) == False
