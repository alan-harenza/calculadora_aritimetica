def artihmetc_arranger(problems, result_parameter=False):
    '''
    input: a list with our problems
        the pattern should be 1"50 + 45", so, number, space, operator, space, number

        result_parameter:
            can be True - show the result of the operation
                    False - don't show the operation
    
    output: formated output according to the problem
    '''
    # seeing the size of our list, following the given rules, if above 5, quit the problem
    if len(problems) > 5:
        print('Error: Too many problems')
        quit()

    for problem in problems:
        operator_list = ['+', '-']
        separation = problem.split()

        # any operator different than + and - must not be included
        if separation[1] not in operator_list:
            print("Error: Operator must be '+' or '-'.")
            quit()

        # must only receive numbers
        if not separation[0].isnumeric() or not separation[2].isnumeric():
            print('Error: Numbers must only contain digits.')
            quit()

        # must have maximum of 4 digit each number
        if len(separation[0]) >=5 or len(separation[2]) >= 5:
            print('Error: Numbers cannot be more than four digits.')
            quit()
    
    primeira_linha = ''
    segunda_linha = ''
    linha_pontilhada = ''
    linha_resultados = ''
    resultado = ''

    for problem in problems:
        separation = problem.split()

        if separation[1]== '+':
            operation_result = str(int(separation[0]) + int(separation[2]))
            middle_space = ' '
        else:
            operation_result = str(int(separation[0]) - int(separation[2]))
            middle_space = ' '
        
        if primeira_linha == '':
            initial_space = ' '
        else:
            initial_space = 4*' '

        if len(separation[0]) > len(separation[2]):
            primeira_linha += initial_space + 2*' ' + separation[0].rjust(2)
            segunda_linha += initial_space + separation[1] + ' ' + separation[2].rjust(len(separation[0]))
            linha_pontilhada += initial_space +(2+len(separation[0])) * '-'
            linha_resultados += initial_space + middle_space +operation_result.rjust(1 + len(separation[0]))

        elif len(separation[0]) == len(separation[2]):
            primeira_linha += initial_space + 2*' ' + separation[0].rjust(2)
            segunda_linha += initial_space + separation[1] + ' ' + separation[2].rjust(2)
            linha_pontilhada += initial_space + (2+len(separation[0])) * '-'
            linha_resultados += initial_space + middle_space +operation_result.rjust(1+ len(separation[0]))

        else:
            primeira_linha += initial_space + 2*' ' + separation[0].rjust(len(separation[2]))
            segunda_linha += initial_space + separation[1] + ' ' + separation[2].rjust(2)
            linha_pontilhada += initial_space + (2+len(separation[2])) * '-'
            linha_resultados += initial_space + middle_space +operation_result.rjust(1+ len(separation[2]))
        
    if result_parameter == True:
        resultado = (primeira_linha + '\n' + segunda_linha + '\n' + linha_pontilhada + '\n' + linha_resultados)
    else:
        resultado = (primeira_linha + '\n' + segunda_linha + '\n' + linha_pontilhada)

    return resultado
