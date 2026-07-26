class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if set(s)!=set(t):
            return False
        s_dict=dict()
        t_dict=dict()
        s_list=list(s)
        for char in s:
            if char in  s_dict:
                s_dict[char]+=1
            else:
                s_dict[char]=1

        for ch in t:
            if ch in t_dict:
                t_dict[ch]+=1
            else:
                t_dict[ch]=1
        if s_dict!=t_dict:
            return False
        
        for char in t:
            if char not in s:
                return False
        return True




