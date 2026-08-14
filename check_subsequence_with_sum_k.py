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

        class Solution:
            def checkSubsequenceSum(self, arr, k):
                # code here
                total=0
                subset=[]
                result=[]
                def solve(ind,total):
                    if total==k:
                        return True
                    elif total>k:
                        return False
                    if ind>=len(arr):
                        return False
                    subset.append(arr[ind])
                    pick=solve(ind + 1, total + arr[ind])
                    if pick==True:
                        return True
                    subset.pop()
                    not_pick=solve(ind + 1, total)
                    return not_pick
                return solve(0, 0)

        class Solution:
            def checkSubsequenceSum(self, arr, k):
                # code here
                total=0
                def solve(ind,total):
                    if total==k:
                        return True
                    elif total>k:
                        return False
                    if ind>=len(arr):
                        return False
                    pick=solve(ind + 1, total + arr[ind])
                    if pick==True:
                        return True
                    not_pick=solve(ind + 1, total)
                    return not_pick
                return solve(0, 0)
