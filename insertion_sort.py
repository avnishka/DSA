new = [3, 5, 6, 4, 8, 9, 10, 7, 1]


# self try
# def insertion_sort(nums):
#     n = len(nums)
#     i = 1
#     while i < n:
#         if nums[i] > nums[i - 1]:
#             i += 1
#         else:
#             j = i - 1
#             key = nums[i]
#             while nums[j] > key and j >= 0:
#                 nums[j + 1] = nums[j]
#                 j -= 1
#             nums[j + 1] = key
#     return nums


# print(insertion_sort(new))


# method by  sir
# def insertion_sort(nums):
# n = len(nums)
# for i in range(1, n):
# key = nums[i]
# j = i - 1
# while j >= 0 and nums[j] > key:
# nums[j + 1] = nums[j]
# j -= 1
# nums[j + 1] = key
# return nums


# print(insertion_sort(new))


# in descending order
def insertion_desc(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


print(insertion_desc(new))
