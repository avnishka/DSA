def findMin(self, nums: List[int]) -> int:
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
