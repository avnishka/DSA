from binary_search import solution


class Solution:
    def countFreq(self, arr, target):
        # code here
        return self.searchRange(arr, target)

    def searchRange(self, arr, target):

        first = self.lb(arr, target)

        if first == len(arr) or first == -1 or arr[first] != target:
            return 0

        last = self.ub(arr, target)
        return last - first

    def lb(self, arr, target):
        n = len(arr)
        low = 0
        high = n - 1
        first = n
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                first = mid
                high = mid - 1
            else:
                low = mid + 1
        return first

    def ub(self, arr, target):
        n = len(arr)
        low = 0
        high = n - 1
        last = n
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                last = mid
                high = mid - 1
            else:
                low = mid + 1
        return last

    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    print(Solution().countFreq(nums, 3))
