expressions = ["28 + 18", "100 * 36"]
first_number = []
second_number = []
operation_row = []

for expression in expressions:
    separation = expression.split()
    # print(separation)
    first_number.append(separation[0])
    operation_row.append(separation[1])
    second_number.append(separation[2])
    for sign_operation in operation_row:
        if sign_operation == "/" or sign_operation == "*":
            print("invalid sign operation")
            quit()
    for number_first_row in first_number:
        if not number_first_row.isnumeric():
            print("must have only numbers")
            quit()
    for number_second_row in second_number:
        if not number_second_row.isnumeric():
            print("must have only numbers")
            quit()
