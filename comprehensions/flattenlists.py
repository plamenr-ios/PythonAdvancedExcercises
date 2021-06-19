data = input().split("|")
data = data[::-1]  # or reverse()
result = [value.strip() for i in range(len(data)) for value in data[i].split()]
print(*result)