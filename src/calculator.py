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

    def multiply(numbers = []):
        if len(numbers) == 0:
            return 0

        multiply = None
        for number in numbers:
            if multiply == None:
                multiply = number
            else:
                multiply *= number
        return round(multiply, 2)
