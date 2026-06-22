# new = [5, 8, 1, 6, 9, 2, 4]


# def bubble_sort(nums):
#     n = len(nums)
#     for i in range(n - 2, 0, -1):
#         j = 0
#         while j <= i:
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             j += 1
#     return nums


# print(bubble_sort(new))


# optimised version
#
# def bubble_sort(nums):
#     n = len(nums)
#     for i in range(n - 1, 0, -1):
#         is_swapped = False
#         j = 0
#         while j < i:
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#                 is_swapped = True
#             j += 1
#         if is_swapped == False:
#             break
#     return nums


# new2 = [1, 2, 3, 4, 5, 6, 7]
# print(bubble_sort(new2))

# bubble sort for descending order
def bubble_sort_desc(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        is_swapped = False
        j = 0
        while j < i:
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True
            j += 1

        if is_swapped == False:
            break
    return nums


new2 = [1, 2, 3, 4, 5, 6, 7]
print(bubble_sort_desc(new2))
