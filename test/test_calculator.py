from ..src.calculator import *

class TestCalculator:

    @staticmethod
    def testSum():
        # arrange
        number1 = 1
        number2 = 2
        expectedSum = 3
        # act
        sum = Calculator.sum(number1, number2)
        # assert
        assert sum == expectedSum