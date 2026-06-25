# brute force method
# # def longestConsecutive(nums):
#     n = len(nums)
#     maxi = 0
#     for j in range(n):
#         num = nums[j]
#         count = 1
#         while num + 1 in nums:
#             count += 1
#             num = num + 1
#         maxi = max(count, maxi)
#     return maxi

# method 2
# def longestConsecutive(nums):
#     n = len(nums)
#     num_set = set(nums)
#     longest = 0
#     for num in num_set:
#         if num - 1 not in num_set:
#             x = num
#             streak = 1
#             while x + 1 in num_set:
#                 x += 1
#                 streak += 1

#             longest = max(longest, streak)

#     return longest


# method 3
def longestConsecutive(nums):
    nums.sort()
    longest = 0
    count = 0
    last = float("-inf")
    n = len(nums)
    for i in range(n):
        num = nums[i]
        if num - 1 == last:
            count += 1
            last = num
        elif num != last:
            count = 1
            last = num
        longest = max(longest, count)
    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
