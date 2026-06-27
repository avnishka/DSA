def searchInsert(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    if target > nums[high]:
        return high + 1
    elif target < nums[low]:
        return low


nums = [1, 2, 4, 6, 8, 10]
result = searchInsert(nums, 5)
print(result)
