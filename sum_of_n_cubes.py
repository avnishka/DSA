class Solution:
    def sumOfSeries(self, n):
        # code here
        if n == 1:
            return 1
        return self.summing(0, 1, n)

    def summing(self, sum, i, n):
        if i > n:
            return sum
        return self.summing(sum + i**3, i + 1, n)
