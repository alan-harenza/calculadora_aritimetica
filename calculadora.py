expressions = ["10000 - 36", "28 + 18"]
first_number = []
second_number = []
operation_row = []

# first step, seeing if the problem conditions fits in the scenarios
for expression in expressions:
    if len(expressions) > 5:
        print("Error: Too many problems")
    separation = expression.split()
    # validation of the math operator
    if separation[1] == "/" or expression[1] == "*":
        print("Error: Operator must be '+' or '-'.")
        quit()
    # validation if the first or second sequence (before and after the math
    # operator) is a number
    if not separation[0].isnumeric() or not separation[2].isnumeric():
        print("Error: Number must only conatain digits.")
        quit()
    if len(separation[0]) > 4 or len(separation[2]) > 4:
        print("Error: Numbers cannot be more than four digits")
        quit()
print('validation step is ok to go')
