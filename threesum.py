# brute force TLE error
# def threeSum(nums):
#     n = len(nums)
#     myset = set()
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     new = [nums[i], nums[j], nums[k]]
#                     new.sort()
#                     myset.add(tuple(new))
#     return list(myset)


# better Solution
# def threeSum(nums):
#     n = len(nums)
#     maps = set()
#     for i in range(n):
#         myset = set()
#         for j in range(i + 1, n):
#             temp = -(nums[i] + nums[j])
#             if temp in myset:
#                 new = [nums[i], nums[j], temp]
#                 new.sort()
#                 maps.add(tuple(new))
#             myset.add(nums[j])
#     return list(maps)


# Optimal solution
def threeSum(nums):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n):
        if i != 0 and nums[i - 1] == nums[i]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j - 1] == nums[j]:
                    j += 1
                while j < k and nums[k + 1] == nums[k]:
                    k -= 1
    return ans
