class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_islands = 0
        #n=no of rows , m= no of columns
        n, m = len(grid), len(grid[0])

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]!= "1": #checking for the edge cases
                return 
            else:
                grid[i][j] = "0" #setting the visited node to 0 so we dont revisit them again
                dfs(i,j+1)       #move right
                dfs(i,j-1)       #move left
                dfs(i+1,j)       #move up
                dfs(i-1,j)       #move down
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    number_islands += 1 #incrementing the count of islands
                    dfs(i,j)            # recursion
        return number_islands
        

        # time complexity = O(m*n)
        # space complexity = O(m*n)