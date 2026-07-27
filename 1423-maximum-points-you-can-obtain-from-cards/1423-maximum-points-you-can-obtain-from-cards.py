class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ls=0
        rs=0
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        maxi=0
        for i in range (k):
            ls+=cardPoints[i]
        maxi=max(maxi,ls)
        for i in range(1,k+1):
            ls-=cardPoints[k-i]
            rs+=cardPoints[n-i]
            maxi=max(maxi,ls+rs)
            
        return maxi



        