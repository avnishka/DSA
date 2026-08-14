class Solution:
    def findSubsequenceSum(self, arr, k):
        # code here
        total=0
        subset=[]
        result=[]
        def solve(ind,total):
            if total==k:
                result.append(subset[:])
                return
            elif total>k:
                return
            if ind>=len(arr):
                return
            subset.append(arr[ind])
            solve(ind + 1, total + arr[ind])
            subset.pop()
            solve(ind + 1, total)
        solve(0, 0)
        return result
