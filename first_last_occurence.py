def searchR(nums, target):

    n = len(nums)
    first = -1
    last = -1
    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


# optimised
def searchRange(nums, target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]

    last = ub(nums, target) - 1
    return [first, last]


def lb(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    first = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            first = mid
            high = mid - 1
        else:
            low = mid + 1
            return first


def ub(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    last = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            last = mid
            high = mid - 1
        else:
            low = mid + 1
    return last


nums = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3
print(searchRange(nums, target))
