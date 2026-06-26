# def rotate(matrix):
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     rows = len(matrix)
#     cols = len(matrix[0])
#     result = [[0] * rows for _ in range(cols)]
#     k = cols
#     for i in range(rows):
#         k -= 1
#         for j in range(cols):
#             if k >= 0:
#                 result[j][k] = matrix[i][j]

#     for i in range(rows):
#         for j in range(cols):
#             matrix[i][j] = result[i][j]
#     return matrix


def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()


nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotate(nums)
print(nums)
