class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        res = 0
        m, n = len(grid), len(grid[0])


        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            # (i,j) 的上下左右
            for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                # 只对在边界上的 坐标进行操作
                # if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 :
                # print(i,j,x,y)
                dfs(grid, x, y)

        # 把边界上的岛屿给淹掉
        for i in range(m):
            dfs(grid, i, 0)
            dfs(grid, i, n - 1)
        for j in range(n):
            dfs(grid, 0, j)
            dfs(grid, m - 1, j)

        # print(grid)
        for i in range(m):
            for j in range(n):
                # 如果发现了一个岛屿，岛屿数量+1
                # 并且把岛屿给淹了
                if grid[i][j] == 1:
                    res += 1
#                    dfs(grid, i, j)
        return res
