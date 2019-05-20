from ..src.calculator import *

class TestCalculator:
    #------ Sum tests -----#
    @staticmethod
    def test_sum():
        # arrange
        number1 = 1
        number2 = 2
        expectedSum = 3
        # act
        sum = Calculator.sum([number1, number2])
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_sum_without_number2():
        # arrange
        number1 = 1
        expectedSum = 1
        # act
        sum = Calculator.sum([number1])
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_sum_without_params():
        # arrange
        expectedSum = 0
        # act
        sum = Calculator.sum()
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_sum_with_negative_numbers():
        # arrange
        number1 = -1
        number2 = -2
        expectedSum = -3
        # act
        sum = Calculator.sum([number1, number2])
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_sum_with_float_numbers():
        # arrange
        number1 = 1.0
        number2 = 2.3
        expectedSum = 3.3
        # act
        sum = Calculator.sum([number1, number2])
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_sum_for_X_numbers():
        # arrange
        number1 = 3
        number2 = 2
        number3 = 4
        number4 = 1
        expectedSum = 10
        # act
        sum = Calculator.sum([number1, number2, number3, number4])
        # assert
        assert sum == expectedSum

    #------ Subtract tests -----#
    @staticmethod
    def test_subtract():
        # arrange
        number1 = 2
        number2 = 1
        expectedSum = 1
        # act
        sum = Calculator.subtract(number1, number2)
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_subtract_without_number2():
        # arrange
        number1 = 2
        expectedSum = 2
        # act
        sum = Calculator.subtract(number1)
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_subtract_without_params():
        # arrange
        expectedSum = 0
        # act
        sum = Calculator.subtract()
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_subtract_with_negative_numbers():
        # arrange
        number1 = -2
        number2 = -1
        expectedSum = -1
        # act
        sum = Calculator.subtract(number1, number2)
        # assert
        assert sum == expectedSum

    @staticmethod
    def test_subtract_with_float_numbers():
        # arrange
        number1 = 2.4
        number2 = 1.2
        expectedSum = 1.2
        # act
        sum = Calculator.subtract(number1, number2)
        # assert
        assert sum == expectedSum