class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        x=len(nums)
        y=1<<x
        new:list[[int]]=[]
        for num in range(y):
            ls=[]
            for i in range(x):
                if num & (1<<i)!=0:
                    ls.append(nums[i])
            new.append(ls)
        return new
