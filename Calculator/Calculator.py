class Calculator:
    def splitExpression(self, expression):
        result = []
        numberValue = ""
        for i in range(len(expression)):
            if expression[i] == " ":
                continue
            elif expression[i].isdigit():
                numberValue += expression[i]
            else:
                result.append(int(numberValue))
                numberValue = ""
                result.append(expression[i])

        result.append(int(numberValue))

        print(expression)
        print(result)
        return result

    def eval(self, expression):
        expressionArray = self.splitExpression(expression)

        sumValue = 0
        sign = 1

        while len(expressionArray) > 1:
            if (expressionArray[1] == '-'):
                sumValue =+ expressionArray[0] * sign
                sign = -1
                expressionArray.pop(0)
                expressionArray.pop(0)
            elif (expressionArray[1] == '+'):
                sumValue += expressionArray[0] * sign
                sign = 1
                expressionArray.pop(0)
                expressionArray.pop(0)
            elif(expressionArray[1] == '*'):
                expressionArray[0] = expressionArray[0] * expressionArray[2]
                expressionArray.pop(1)
                expressionArray.pop(1)
            elif(expressionArray[1] == '/'):
                expressionArray[0] = expressionArray[0] // expressionArray[2]
                expressionArray.pop(1)
                expressionArray.pop(1)
            print("sumValue: ", sumValue)
            print("sign: ", sign)
            print("list: ", expressionArray)

        if len(expressionArray) > 0:
            sumValue += expressionArray.pop(0) * sign

        return sumValue

calculator = Calculator()
expresssion = "2 - 3 * 4 + 10 / 2" # -5
result = calculator.eval(expresssion)
print(result)

"""
expression = 2 - 3 * 4 + 10 / 2
[2, '-', 3, '*', 4, '+', 10, '/', 2]
sumValue:  2
sign:  -1
list:  [3, '*', 4, '+', 10, '/', 2]
sumValue:  2
sign:  -1
list:  [12, '+', 10, '/', 2]
sumValue:  -10
sign:  1
list:  [10, '/', 2]
sumValue:  -10
sign:  1
list:  [5]

result = -5
"""
