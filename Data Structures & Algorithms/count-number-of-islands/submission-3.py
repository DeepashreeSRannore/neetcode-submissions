class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0
        n = len(grid)
        m = len(grid[0])
    
        def dfs(i,j):
            #edge casee handling
            if i<0 or j<0 or i>=n or j>=m or grid[i][j] != "1":
                return
            
            grid[i][j] = "0" #inplace making of visited ceel to 0
            dfs(i,j+1)       #move right
            dfs(i,j-1)       #move left
            dfs(i+1,j)       #move up
            dfs(i-1,j)       #move down 
        
        for i in range(n):         # n times
            for j in range(m):     # m times
                if grid[i][j]=="1":
                    total_islands += 1
                    dfs(i,j)
        return total_islands

    #total time complexity = O(m*n) = space complexity
        