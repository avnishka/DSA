nums = [2, 5, 3, 6, 8, 90, 6, 3, 2, 5, 1]


# right rotation in one place
#  method 1
# def rotate_right(arr):
#     n = len(arr)
#     # arr[:] = arr[-1:] + arr[: n - 1]
#     arr = arr[n - 1 :] + arr[: n - 1]
#     return arr


# method 2
def rotate_right(arr):
    n = len(arr)
    temp = arr[n - 1]
    for i in range(n - 2, -1, -1):
        arr[i + 1] = arr[i]
    arr[0] = temp
    return arr


print(rotate_right(nums))


# rotate left by one place
# method1
# def rotate_left(arr):
#     n = len(arr)
#     arr[:] = arr[1:] + arr[:1]
#     return arr


# method2
def rotate_left(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = temp
    return arr


print(rotate_left(nums))
