expressions = ["100 - 36", "28 + 18"]
first_number = []
second_number = []
operation_row = []

# first step, seeing if the problem conditions fits in the scenarios
for expression in expressions:
    if len(expressions) > 5:
        print("too many expressions!")
    separation = expression.split()
    # validation of the math operator
    if separation[1] == "/" or expression[1] == "*":
        print("invalid sign operation")
        quit()
    # validation if the first sequence of before the math operator is a number
    if not separation[0].isnumeric():
        print("must have only numbers before the sign operation")
        quit()
    # validation if the second sequence of after the math operator is a number
    if not separation[2].isnumeric():
        print("must have only numbers after the sign operation")
        quit()
# print('validation step is ok to go')
