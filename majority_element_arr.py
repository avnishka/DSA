def majorityElement(nums):
    n = len(nums)
    map = {}
    for num in nums:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    for key, value in map.items():
        if value > n // 2:
            return key


nums = [3, 2, 3]
print(majorityElement(nums))
