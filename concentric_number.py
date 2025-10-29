n = 5
size = 2 * n - 1
matrix = [[0] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        min_dist = min(i, j, size - i - 1, size - j - 1)
        matrix[i][j] = str(n - min_dist)
for row in matrix:
    print(' '.join(row))
