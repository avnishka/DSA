# brute force
# def rearrangeArray(nums):
#     new = []
#     pos = []
#     neg = []
#     n = len(nums)
#     i = 0
#     j = 0
#     for k in range(n):
#         if nums[k] > 0:
#             pos.append(nums[k])
#         else:
#             neg.append(nums[k])
#     while len(new) != n:
#         new.append(pos[i])
#         new.append(neg[j])
#         i += 1
#         j += 1
#     return new

# better way
def rearrangeArray(nums):
    pos = []
    neg = []
    n = len(nums)
    for k in range(n):
        if nums[k] >= 0:
            pos.append(nums[k])
        else:
            neg.append(nums[k])
    for i in range(len(pos)):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]
    return nums


nums = [1, 2, 0, -3, -8, -1]
print(rearrangeArray(nums))
