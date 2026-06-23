nums = [3, 5, 6, 8, 9, 10, 20]


def checksorted(arr):
    i = 0
    n = len(arr)
    while i < n - 1:
        if arr[i] < arr[i + 1]:
            i += 1
        else:
            return False
    return True


print(checksorted(nums))
