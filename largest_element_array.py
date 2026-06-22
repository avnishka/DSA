def largest(arr):

    largest = float("-inf")

    for i in range(len(arr)):
        largest = max(largest, arr[i])
    return largest


nums = [2, 6, 3, 5, 8, 3, 7, 0, 4, 2, 12, 5, 7]
print(largest(nums))
