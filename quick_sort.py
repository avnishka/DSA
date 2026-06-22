def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)
    return arr


nums = [2, 6, 3, 5, 8, 3, 7, 0, 4, 2, 12, 5, 7]
print(quick_sort(nums, 0, len(nums) - 1))
