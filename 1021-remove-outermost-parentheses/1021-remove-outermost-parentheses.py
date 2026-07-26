class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        count=0
        for char in s:
            if char=="(":
                if count>0:
                    ans=ans+char
                count+=1
            elif char==")":
                count-=1
                if count>0:
                    ans=ans+char
        return ans

        