nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


print(linear_search(nums, 5))
