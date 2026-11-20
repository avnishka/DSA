class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        subset=[]
        nums=[1,2,3,4,5,6,7,8,9]
        def solve(ind,k,n):
            if k==0 and n!=0:
                return
            elif k==0 and n==0:
                result.append(subset.copy())
                return
            elif ind>=9:
                return

            subset.append(nums[ind])
            solve(ind+1,k-1,n-nums[ind])
            subset.pop()
            solve(ind+1,k,n)

            
        solve(0,k,n)
        return result
            
        