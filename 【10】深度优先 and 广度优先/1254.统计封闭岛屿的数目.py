# 有一个二维矩阵 grid，
# 每个位置要么是陆地（记号为0 ）要么是水域（记号为1 ）。
#
# 我们从一块陆地出发，每次可以往上下左右4 个方向相邻区域走，
# 能走到的所有陆地区域，我们将其称为一座「岛屿」。
#
# 如果一座岛屿完全由水域包围，即陆地边缘上下左右所有相邻区域都是水域，
# 那么我们将其称为 「封闭岛屿」。
#
# 请返回封闭岛屿的数目。
#
class Solution:
    def closedIsland(self, grid) -> int:

        res = 0
        m, n = len(grid), len(grid[0])

        # 从 (i,j) 开始，将与之相邻的 ‘0’ 都变为 ‘1’
        def dfs(grid, i, j):
            if i<0 or j< 0 or i>=m or j>=n:
                return
            if grid[i][j] == 1:
                return
            grid[i][j] = 1
            # (i,j) 的上下左右
            for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                # 只对在边界上的 坐标进行操作
                #if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 :
                    # print(i,j,x,y)
                    dfs(grid, x, y)

        # 把边界上的岛屿给淹掉
        for i in range(m):
            dfs(grid,i,0)
            dfs(grid,i,n-1)
        for j in range(n):
            dfs(grid,0,j)
            dfs(grid,m-1,j)

       # print(grid)
        for i in range(m):
            for j in range(n):
                # 如果发现了一个岛屿，岛屿数量+1
                # 并且把岛屿给淹了
                if grid[i][j] == 0:
                    res += 1
                    dfs(grid, i, j)
        return res

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
sol = Solution()
print(sol.closedIsland(grid))