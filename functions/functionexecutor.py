def func_executor(*args):
    result = []
    for i in range(len(args)):
        data = args[i][1]
        result1 = args[i][0](*data)
        result.append(result1)
    return result
