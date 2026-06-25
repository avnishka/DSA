# brute force
# def setZeroes(matrix):
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     row = len(matrix)
#     col = len(matrix[0])
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j] == 0:
#                 self.markinf(matrix, i, j)
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j] == float("-inf"):
#                 matrix[i][j] = 0
#     return matrix


# def markinf(self, matrix, x, y):
#     r = len(matrix)
#     c = len(matrix[0])
#     for i in range(r):
#         if matrix[i][y] != 0:
#             matrix[i][y] = float("-inf")
#     for j in range(c):
#         if matrix[x][j] != 0:
#             matrix[x][j] = float("-inf")
#     return matrix


# optimal method
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    r = len(matrix)
    c = len(matrix[0])
    rowtrack = [0 for _ in range(r)]
    coltrack = [0 for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rowtrack[i] = -1
                coltrack[j] = -1
    for i in range(r):
        for j in range(c):
            if rowtrack[i] == -1 or coltrack[j] == -1:
                matrix[i][j] = 0
    return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(setZeroes(matrix))
