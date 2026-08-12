class Solution:
    def setBit(self, n):
        # code here
        n = n | (n-1)
        return n
