# self try

new = [5, 7, 8, 4, 1, 6, 9, 2]
# for i in range(len(nums)):
#     min_index = i
#     j = i + 1
#     while j < len(nums):
#         if nums[i] <= nums[j]:
#             j += 1
#         else:
#             if nums[min_index] > nums[j]:
#                 min_index = j
#             j += 1
#     nums[i], nums[min_index] = nums[min_index], nums[i]
# print(nums)


# by recursion
def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selection_sort(new))
