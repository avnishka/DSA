class Solution:
    def findMin(self, n):
        # code here
        new = [1, 2, 5, 10]
        m = len(new)
        remain = n
        count = 0
        while remain != 0:
            for i in range(m - 1, -1, -1):
                if new[i] <= remain:
                    remain -= new[i]
                    count += 1
                    break
        return count
