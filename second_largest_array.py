nums = [2, 6, 3, 5, 8, 3, 7, 0, 4, 2, 12, 5, 7]

# method 1(optimal)
# def second_largest(arr):
#     largest = float("-inf")
#     second = float("-inf")
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             second = largest
#             largest = arr[i]
#         elif arr[i] > second and arr[i] < largest:
#             second = arr[i]
#     return second

# method 2 (2 iterations)
# def second_largest(arr):
#     largest = float("-inf")
#     second = float("-inf")
#     for i in range(len(arr)):
#         largest = max(largest, arr[i])
#     for i in range(len(arr)):
#         if arr[i] > second and arr[i] < largest:
#             second = arr[i]
#     return second


# print(second_largest(nums))


# method3
def second_largest(arr):
    new = sorted(arr)
    return new[-2]


print(second_largest(nums))
