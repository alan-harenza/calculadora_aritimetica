def artihmetc_arranger(problems, result_parameter=False):
    # first step, seeing if the problem conditions fits in the scenario
    if len(problems) > 5:
        print("Error: Too many problems")
    for expression in problems:
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
    # print('validation step is ok to go')

        # second step, identifying the sign operator
    for expressions in problems:
        string_division = expressions.split()
        if string_division[1] == '+':
            # return 'sum'
            if len(string_division[0]) > len(string_division[2]):
                trace_line = len(string_division[0]) * '-' + 2 * '-'
            elif len(string_division[0]) < len(string_division[2]):
                trace_line = len(string_division[2]) * '-' + 2 * '-'
            elif len(string_division[0]) == len(string_division[2]):
                trace_line = len(string_division[0]) * '-' + 2 * '-'
        return trace_line               


problems = ["1000 + 5"]
test = artihmetc_arranger(problems, False)
print(test)
