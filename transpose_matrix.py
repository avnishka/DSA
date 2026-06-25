nums = [[5, 9, 1], [2, 3, 7]]


def transpose(nums):
    rows = len(nums)
    cols = len(nums[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = nums[i][j]
    return result


print(transpose(nums))
