nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]

# method 1 usinf sc=0(n)
# def move(arr):
#     n = len(arr)
#     temp = []
#     for i in range(n):
#         if arr[i] != 0:
#             temp.append(arr[i])
#     i = 0
#     while i < len(temp):
#         arr[i] = temp[i]
#         i += 1
#     while i < n:
#         arr[i] = 0
#         i += 1
#     return arr


# print(move(nums))


# method 2 using sc=0(1)
def move(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    while j < n:
        arr[j] = 0
        j += 1
    return arr


print(move(nums))
