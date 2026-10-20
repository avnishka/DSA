class Solution:
    def binstr(self, n):
        # code here
        nums=n*["0"]
        result=[]
        def solve(ind,nums,result):
            if ind>=len(nums):
                result.append("".join(nums))
                return
            nums[ind]="0"
            solve(ind+1,nums,result)
            nums[ind]="1"
            solve(ind+1,nums,result)
        solve(0,nums,result)
        return result
        
        
            
                