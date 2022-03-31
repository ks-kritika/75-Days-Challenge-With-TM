class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j,island):
            if(i>=0 and i<n and j>=0 and j<m and grid[i][j] == 1):
                island+=1
                grid[i][j] = 2   #to avoid repetitions
                dfs(grid, i+1, j, island)
                dfs(grid, i-1, j, island)
                dfs(grid, i, j+1, island)
                dfs(grid, i, j-1, island)
            return island

        res = 0
        temp=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    temp = dfs(grid, i, j, temp)
                    res=max(res, temp)

        return res    