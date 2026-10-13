class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        def solve(ind,total):
            if total==k:
                return True
            if total>k or ind>=len(arr):
                return False
            
            if solve(ind+1,total+arr[ind]):
                return True
            if solve(ind+1,total):
                return True
            return False
        return solve(0,0)
        