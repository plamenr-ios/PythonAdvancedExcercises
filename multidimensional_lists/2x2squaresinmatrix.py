count = [int(x) for x in input().split()]

matrix = []

#       get matrix
for i in range(count[0]):
    matrix.append([x for x in input().split()])

#       get matches from top to bottom rows
matches = 0
for i in range(count[0]):
    for j in range(count[1]):
        current_symbol = matrix[i][j]
        if i < len(matrix) - 1:
            down_symbol = matrix[i+1][j]
            if current_symbol == down_symbol:
                if j < count[1] - 1:
                    if matrix[i][j+1] == matrix[i+1][j+1] and current_symbol == matrix[i][j+1]:
                        matches += 1
print(matches)
