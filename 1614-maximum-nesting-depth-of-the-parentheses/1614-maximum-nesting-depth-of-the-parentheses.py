class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxi=float("-inf")
        for ch in s:
            if ch=="(":
                count+=1
            if ch==")":
                count-=1
            
            maxi=max(maxi,count)
        return maxi
        