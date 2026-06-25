from upper_triangle import nums


def lower_triangle(nums):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(rows):
        for j in range(cols):
            if j <= i:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()


print(lower_triangle(nums))
