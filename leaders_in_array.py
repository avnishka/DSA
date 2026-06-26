# brute force
# def leaders(arr):
#     # code here
#     n = len(arr)
#     ans = []
#     for i in range(n):
#         leader = True
#         for j in range(i + 1, n):
#             if arr[j] > arr[i]:
#                 leader = False
#                 break
#         if leader == True:
#             ans.append(arr[i])
#     return ans


# arr = [16, 17, 4, 3, 5, 2]
# print(leaders(arr))

# better approach
def leaders(arr):
    # code here
    n = len(arr)
    ans = []
    maxi = float("-inf")
    for i in range(n - 1, -1, -1):
        if arr[i] >= maxi:
            ans.append(arr[i])
            maxi = arr[i]
    return ans[::-1]


arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))
