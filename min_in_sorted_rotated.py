def findMini(nums):
    low = 0
    high = len(nums) - 1
    mini = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= nums[high]:
            low = mid + 1
            mini = min(nums[high], mini, nums[mid])
        elif nums[mid] < nums[high]:
            high = mid - 1
            mini = min(nums[low], mini, nums[mid])
    return mini


def findMin(nums):
    low = 0
    high = len(nums) - 1
    mini = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= nums[high]:
            mini = min(mini, nums[mid])
            high = mid - 1
        else:
            mini = min(mini, nums[low])
            low = mid + 1
    return mini


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))
print(findMini(nums))
