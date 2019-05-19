from ..src.calculator import *

class TestCalculator:

    @staticmethod
    def test_sum():
        # arrange
        number1 = 1
        number2 = 2
        expectedSum = 3
        # act
        sum = Calculator.sum(number1, number2)
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_sum_without_number2():
        # arrange
        number1 = 1
        expectedSum = 1
        # act
        sum = Calculator.sum(number1)
        # assert
        assert sum == expectedSum