class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        result=[]

        def solve(ind:int):
            if ind>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[ind])
            solve(ind+1)
            subset.pop()
            solve(ind+1)
        
        solve(0)
        return result



        