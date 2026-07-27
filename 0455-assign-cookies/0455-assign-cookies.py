class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        g.sort()
        s.sort()
        l=0
        n=len(g)
        m=len(s)
        r=0
        while l<n and r<m:
            if g[l]<=s[r]:
                l+=1
                count+=1
            r+=1
        return count
        