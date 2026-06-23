from typing import List

# brute force
# def missingNumber(nums: List[int]) -> int:
#     n = len(nums)
#     for i in range(0, n + 1):
#         if i not in nums:
#             return i


# using  dict better method
# def missingNumber(nums: List[int]) -> int:
#     n = len(nums)
#     new = {}
#     for i in range(0, n + 1):
#         new[i] = 0
#     for num in nums:
#         new[num] = 1
#     for a, b in new.items():
#         if b == 0:
#             return a


# optimal solution
def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


print(missingNumber([3, 0, 1]))
