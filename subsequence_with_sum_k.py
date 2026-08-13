class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        result=[]
        subset=[]
        total=0

        def solve(ind,total:int):
            if total==k:
                return True
            elif total > k:
                return
            if ind>=len(arr):
                return
            if solve(ind + 1, total + arr[ind]):
                return True
            if solve(ind + 1, total):
                return True

            return False

        return solve(0, 0)
