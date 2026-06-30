class Solution:
    def printTillN(self, n):
        # code here
        return self.num(1, n)

    def num(self, i, n):
        if i > n:
            return
        print(i, end=" ")
        self.num(i + 1, n)
