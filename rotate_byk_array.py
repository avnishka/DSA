# def rotate(nums, k):
#     n = len(nums)
#     rotations = k % n
#     for _ in range(rotations):
#         x = nums.pop()
#         nums.insert(0, x)
#     return nums


# def rotate(self, nums: List[int], k: int) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     n = len(nums)
#     k = k % n
#     left_side = self.reverse(nums[: n - k])
#     right_side = self.reverse(nums[n - k :])
#     nums[:] = left_side + right_side
#     nums[:] = self.reverse(nums)
#     return

# def reverse(self, arr):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         right -= 1
#         left += 1
#     return arr

# optimal
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[n - k :] + nums[: n - k]
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)
