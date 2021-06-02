count = int(input())

curr_sum = 0
values = set()
odd_value = set()

for i in range(1, count + 1):
    name = input()
    for j in name:
        curr_sum += ord(j)
    curr_sum = int(curr_sum / i)
    if curr_sum % 2 == 0:
        values.add(curr_sum)
    else:
        odd_value.add(curr_sum)
    curr_sum = 0

sym = values.symmetric_difference(odd_value)
dif = odd_value.difference(values)
uni = values.union(odd_value)

if sum(values) > sum(odd_value):
    print(", ".join([str(x) for x in sym]))
elif sum(values) < sum(odd_value):
    print(", ".join([str(x) for x in dif]))
else:
    print(", ".join([str(x) for x in uni]))

