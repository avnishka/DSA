class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxi=0
        stack=[]
        for ch in s:
            if ch=="(":
                count+=1
                stack.append("(")
                maxi=max(maxi,count)
            if ch==")":
                count-=1
                stack.pop()
        return maxi
        