# reverse an array without Recursion
# num = [5, 7, 3, 2, 6, 1, 5, 9]
# new = []
# left, right = 2, 5
# r = right

# for i in range(len(num)):
#     if i < left or i > right:
#         new.append(num[i])
#     else:
#         new.append(num[r])
#         r -= 1

# print(new)

# reversing by recursion
num = [5, 7, 3, 2, 6, 1, 5, 9]


# def reversing(nums, left, right):
#     if right < left or left == right:
#         return
#     nums[left], nums[right] = nums[right], nums[left]
#     reversing(nums, left + 1, right - 1)
#     return nums


# print(reversing(num, 0, len(num) - 1))


# with 1 based indexing
class Solution:
    def reverseSubArray(self, arr, l, r):
        l -= 1
        r -= 1

        def helper(left, right):
            if left >= right:
                return

            arr[left], arr[right] = arr[right], arr[left]
            helper(left + 1, right - 1)

        helper(l, r)
        return arr
