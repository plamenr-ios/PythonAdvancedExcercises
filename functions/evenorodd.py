def even_odd(*args):
    if args[-1] == "even":
        return [int(x) for x in args[0:-1] if int(x) % 2 == 0]
    else:
        return [int(x) for x in args[0:-1] if not int(x) % 2 == 0]
