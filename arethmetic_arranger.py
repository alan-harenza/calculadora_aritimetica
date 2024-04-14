def artihmetc_arranger(problems, result_parameter=False):
    first_line = []
    second_line = []
    operation_sign = []
    result_line = []
    dot_line = []

    # first step, seeing if the problem conditions fits in the scenario
    for expression in problems:
        if len(problems) > 5:
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
    # print('validation step is ok to go')

    # second step, identifying the sign operator
        if separation[1] == '+':
            # return 'sum'
            if result_parameter is False:
                # return 'dont show result'
                pass

            elif result_parameter is True:
                # return 'show result'
                pass

        elif separation[1] == '-':
            # return 'subtraction'
            if result_parameter is False:
                # return 'dont show result'
                pass

            elif result_parameter is True:
                # return 'show result'
                pass


problems = ["25 + 18"]
test = artihmetc_arranger(problems, True)
print(test)
