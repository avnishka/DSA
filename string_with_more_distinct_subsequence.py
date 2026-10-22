class Solution:
    def betterString(self, s1, s2):
        # Code here
        def distinctchars(s:str):
            count=1
            seen={}
            for ch in s:
                new_count=2*count
                if ch in seen:
                    new_count-=seen[ch]
                seen[ch]=count
                count=new_count
            return count
        c1=distinctchars(s1)
        c2=distinctchars(s2)
        return s1 if c1 >= c2 else s2