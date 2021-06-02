text = input()

histogram = {}
for letter in text:
    if letter not in histogram:
        histogram[letter] = 0
    histogram[letter] += 1

for key, value in sorted(histogram.items()):
    print(f"{key}: {value} time/s")
