nums = [1, 2, 2, 3, 4, 4, 5]


# menthod 1 brute force
# def remove_duplicates(arr):
#     n = len(nums)
#     map = {}
#     for i in range(n):
#         map[arr[i]] = 0
#     j = 0
#     for key in map:
#         arr[j] = key
#         j += 1
#     return j


# print(remove_duplicates(nums))


# method2 optimal
def remove_duplicates(arr):
    n = len(arr)
    if n == 1:
        return 1
    i = 0
    j = i + 1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    return i + 1


print(remove_duplicates(nums))
