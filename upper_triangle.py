nums = [[5, 10, 8], [10, 6, 3], [2, 1, 9]]


def upper_traingle(nums):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(rows):
        for j in range(cols):
            if j >= i:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()


print(upper_traingle(nums))
