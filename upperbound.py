def upperBound(arr, x, n) -> int:
    # Write your code here.
    low = 0
    high = n - 1
    ub = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub


nums = [1, 2, 4, 6, 8, 10]
result = upperBound(nums, 5, len(nums))
print(result)
