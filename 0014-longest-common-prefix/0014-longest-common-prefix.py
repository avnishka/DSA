class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs=="":
            return
        base=strs[0]
        ans=""
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i==len(word) or base[i]!=word[i]:
                    return ans
            ans+=base[i]
        return ans



        