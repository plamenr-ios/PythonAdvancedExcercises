odd_or_even = input()
numbers = [int(x) for x in input().split()]

if odd_or_even == "Odd":
    odds = [x for x in numbers if not x % 2 == 0]
    print(sum(odds) * len(numbers))
else:
    evens = [x for x in numbers if x % 2 == 0]
    print(sum(evens) * len(numbers))