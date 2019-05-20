class Calculator:
    def sum(numbers = []):
        sum = 0
        for number in numbers:
            sum += number
        return sum

    def subtract(numbers = []):
        if len(numbers) == 0:
            return 0

        subtract = None
        for number in numbers:
            if subtract == None:
                subtract = number
            else:
                subtract -= number
        return subtract

    def multiply(number1, number2 = 1):
        return round(number1 * number2, 2)
