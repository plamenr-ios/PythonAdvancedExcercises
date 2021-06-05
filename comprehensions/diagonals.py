n = int(input())
matrix = []
primary = []
secondary = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

for i in range(len(matrix)):
    primary.append(int(matrix[i][i]))

#       get bottom left to top right diagonal from matrix
corr_i = 0
for i in range(len(matrix) -1, -1, -1):
    secondary.append(int(matrix[corr_i][i]))
    corr_i += 1

print(f"First diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Second diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")