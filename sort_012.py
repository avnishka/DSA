def sort012(arr):
    # code here
    zero = 0
    one = 0
    two = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        elif arr[i] == 1:
            one += 1
        else:
            two += 1
    arr[:] = (
        [0 for _ in range(zero)] + [1 for _ in range(one)] + [2 for _ in range(two)]
    )
    return arr


arr = [0, 2, 1, 2, 1, 0]
print(sort012(arr))
