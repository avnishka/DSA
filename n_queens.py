class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        board=["."*n for _ in range(n)]
        self.solve(0,ans,board,n)
        return ans
    
    def solve(self,col,ans,board,n):
        if col==n:
            ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                self.solve(col+1,ans,board,n)
                board[row]=board[row][:col]+"."+board[row][col+1:]
    
    def isSafe(self,row,col,board,n):
        duprow=row
        dupcol=col
        while row>=0 and col>=0:
            if board[row][col]=="Q":
                return False
            row-=1
            col-=1
        row=duprow
        col=dupcol
        while col>=0:
            if board[row][col]=="Q":
                return False
            col-=1
        col=dupcol
        while row<n and col>=0:
            if board[row][col]=="Q":
                return False
            row+=1
            col-=1
        return True

        