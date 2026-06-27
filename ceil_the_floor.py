def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor = -1
    ceil = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            floor = a[mid]
            ceil = a[mid]
            return floor, ceil
        elif a[mid] >= x:
            ceil = a[mid]
            high -= 1
        else:
            floor = a[mid]
            low += 1
    return floor, ceil


nums = [1, 2, 4, 6, 8, 10]
result = getFloorAndCeil(nums, len(nums), 5)
print(result)
