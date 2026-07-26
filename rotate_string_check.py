class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if len(s) != len(goal):
            return False
        result = ""
        for i in range(n):
            result = s[i:] + s[:i]
            if result == goal:
                return True
        return False
