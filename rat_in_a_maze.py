class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        # code here
        size=len(maze)
        result=[]
        visited=[[0]*size for _ in range(size)]
        
        if maze[0][0]==0:
            return []
        
        def solve(row,col,covered):
            
            if row==size-1 and col==size-1:
                result.append(covered)
                return 
            
            visited[row][col]=1
            
            if row + 1 < size and maze[row + 1][col] == 1 and visited[row + 1][col] == 0:
                solve(row + 1, col, covered + "D")
            
            if col-1>=0 and maze[row][col-1]==1 and visited[row][col-1]==0:
                solve(row,col-1,covered+"L")
            
            if col+1<size and maze[row][col+1]==1 and visited[row][col+1]==0:
                solve(row,col+1,covered+"R")
            
            if row-1>=0 and maze[row-1][col]==1 and visited[row-1][col]==0:
                solve(row-1,col,covered+"U")
                
            visited[row][col] = 0
        
        solve(0, 0, "")
        return result