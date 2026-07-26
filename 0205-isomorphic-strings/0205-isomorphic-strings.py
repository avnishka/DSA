class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_dict=dict()
        my_set=set()
        for i in range (len(s)):
            if s[i] not in my_dict:
                if t[i] in my_set:
                    return False
                my_dict[s[i]]=t[i]
                my_set.add(t[i])
            elif my_dict[s[i]]!=t[i]:
                return False
        return True