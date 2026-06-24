def twoSum(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return i, j


# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     n = len(nums)
#     map = {}
#     for i in range(n):
#         remaining = target - nums[i]
#         if remaining in map:
#             return [map[remaining], i]
#         map[nums[i]] = i
nums = [2, 7, 11, 15]
print(twoSum(nums, 9))
