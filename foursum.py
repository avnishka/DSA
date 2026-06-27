# brute force sol
# def fourSum(nums, target):
#     n = len(nums)
#     if n < 4:
#         return []
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 for l in range(k + 1, n):
#                     if nums[i] + nums[j] + nums[k] + nums[l] == target:
#                         return [nums[i], nums[j], nums[k], nums[l]]
#     return []


# better solution
# def fourSum(nums, target):
#     n = len(nums)
#     myset = set()
#     if n < 4:
#         return []
#     for i in range(n):
#         for j in range(i + 1, n):
#             new = set()
#             for k in range(j + 1, n):
#                 total = nums[i] + nums[j] + nums[k]
#                 fourth = target - total
#                 if fourth in new:
#                     temp = [nums[i], nums[j], nums[k], fourth]
#                     temp.sort()
#                     myset.add(tuple(temp))
#                 new.add(nums[k])

#     return list(myset)


# optimal solution
def fourSum(nums, target):
    n = len(nums)
    nums.sort()
    ans = set()
    if n < 4:
        return []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total < target:
                    k += 1
                elif total > target:
                    l -= 1
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.add(tuple(temp))
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    return list(ans)


nums = []
target = 0
print(fourSum(nums, target))
