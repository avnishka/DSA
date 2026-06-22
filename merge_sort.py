def mer_array(left_side, right_side):
    result = []
    i, j = 0, 0
    n = len(left_side)
    m = len(right_side)
    while i < n and j < m:
        if left_side[i] <= right_side[j]:
            result.append(left_side[i])
            i += 1
        else:
            result.append(right_side[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left_side[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right_side[j])
            j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return mer_array(left, right)


nums = [2, 3, 4, 5, 2, 3, 4, 5, 6, 7, 7, 6, 4, 3]
print(merge_sort(nums))
