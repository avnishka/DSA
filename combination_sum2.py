class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort()
        result=[]
        n=len(candidates)

        def solve(ind,total,subset):
            if total==0:
                result.append(subset.copy())
                return
            if ind>=n or total<0:
                return

            subset.append(candidates[ind])
            solve(ind+1,total-candidates[ind],subset)
            subset.pop()

            while ind+1 < n and candidates[ind]==candidates[ind+1]:
                ind+=1
            solve(ind+1,total,subset)
        solve(0,target,[])
        return result
            
