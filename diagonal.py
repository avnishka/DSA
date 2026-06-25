from upper_triangle import nums

# def diagonal(nums):
#     rows = len(nums)
#     cols = len(nums[0])
#     for i in range(rows):
#         for j in range(cols):
#             if i == j:
#                 print(nums[i][j], end=" ")
#             else:
#                 print("*", end=" ")
#         print()


# diagonal(nums)


# opposite diagonal
def opp_diagonal(nums):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(rows):
        for j in range(cols):
            if i + j == rows - 1:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()


opp_diagonal(nums)
