
class Solution:
    def countSubIslands(self, grid1, grid2) -> int:

        m, n = len(grid1),len(grid1[0])

        def dfs(grid,i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return
            if grid[i][j]== 0:
                return
            grid[i][j] = 0
            for x,y in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                dfs(grid,x,y)

        # 如果grid1中i,j块是水，而grid2中i,j块是陆地，
        # 则淹掉grid2中对应的岛屿
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] ==1:
                    dfs(grid2,i,j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res +=1
                    dfs(grid2,i,j)
        return res
