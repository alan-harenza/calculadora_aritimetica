def artihmetc_arranger(problems, result_parameter=False):
    # first step, seeing if the problem conditions fits in the scenario
    if len(problems) > 5:
        print('Error: Too many problems')
        quit()
      


problems = ["1000 + 5"]
test = artihmetc_arranger(problems, False)
print(test)
