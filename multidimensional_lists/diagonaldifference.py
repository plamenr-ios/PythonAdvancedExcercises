count = int(input())

matrix = []
primary = []
secondary = []

#       get matrix
for i in range(count):
    matrix.append([[x] for x in input().split()])

#       get top left to bottom right diagonal from matrix
for i in range(count):
    primary.append(int(matrix[i][i][0]))

#       get bottom left to top right diagonal from matrix
corr_i = 0
for i in range(count -1, -1, -1):
    secondary.append(int(matrix[i][corr_i][0]))
    corr_i += 1

#       print absolute difference from the sum of both diagonals
print(abs(sum(primary) - sum(secondary)))
