# kadane's algorithm
# def maxSubArray(nums):
#     n = len(nums)

#     maximum = float("-inf")
#     total = 0
#     for i in range(n):
#         total = total + nums[i]
#         maximum = max(total, maximum)
#         if total < 0:
#             total = 0
#     return maximum
nums = [1, 2, 3, 4, 5]


# brute force
def maximumsubarray(nums):
    maxi = float("-inf")
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total = total + nums[j]
            maxi = max(total, maxi)
    return maxi


print(maximumsubarray(nums))
