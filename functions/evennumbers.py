def myfilter(filter_func, sequence):
    filtered = []

    for element in sequence:
        if filter_func(element) is True:
            filtered.append(element)

    return filtered

def is_even(num):
    return num % 2 == 0

print(list(myfilter(is_even, [int(x) for x in input().split()])))

