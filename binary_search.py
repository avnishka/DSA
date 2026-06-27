# iterative
def search1(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    if n == 1:
        if target in nums:
            return 0
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# recuursive
def search(nums, target):
    low = 0
    high = len(nums) - 1
    return solution(nums, low, high, target)


def solution(nums, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return solution(nums, low, mid - 1, target)
    else:
        return solution(nums, mid + 1, high, target)
