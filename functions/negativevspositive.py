numbers = [int(x) for x in input().split()]

negatives = [int(x) for x in numbers if x < 0]
positives = [int(x) for x in numbers if x > 0]

print(sum(negatives))
print(sum(positives))

if abs(sum(positives)) > abs(sum(negatives)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
