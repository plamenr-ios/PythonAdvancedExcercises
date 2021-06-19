def age_assignment(*args, **kwargs):
    dict = {}
    ages = kwargs
    for i in range(0, len(args)):
        dict[args[i]] = ages[args[i][0]]
    return dict
