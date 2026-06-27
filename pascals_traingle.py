from math import factorial


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(0, numRows):
            rows = []
            for j in range(i + 1):
                rows.append(self.combination(i, j))
            ans.append(rows)
        return ans

    def combination(self, i, j):
        return factorial(i) // (factorial(j) * factorial(i - j))
