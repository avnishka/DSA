# method1
nums = [1, 2, 3, 1, 2, 3, 2, 3, 4, 5, 6, 6, 7, 8, 9, 1, 2, 3, 4, 5, 4]
# frequency = dict()
# for i in range(0, len(nums)):
#     if nums[i] in frequency:
#         frequency[nums[i]] += 1
#     else:
#         frequency[nums[i]] = 1
# print(frequency)

# method2
hash_map = {}
n = len(nums)
for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
print(hash_map)
