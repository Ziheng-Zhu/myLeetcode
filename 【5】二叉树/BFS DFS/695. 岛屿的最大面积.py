# 给你一个大小为 m x n 的二进制矩阵 grid 。
#
# 岛屿是由一些相邻的1(代表土地) 构成的组合，
# 这里的「相邻」要求两个 1 必须在
# 水平或者竖直的四个方向上 相邻。
# 你可以假设grid 的四个边缘都被 0（代表水）包围着。
#
# 岛屿的面积是岛上值为 1 的单元格的数目。
#
# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0
#


class Solution:
    def maxAreaOfIsland(self, grid) -> int:

        m, n = len(grid),len(grid[0])

        def dfs(grid,i,j):

            if i<0 or j<0 or i>=m or j>=n:
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1+dfs(grid,i-1,j) + dfs(grid,i,j+1) \
                   + dfs(grid,i+1,j) + dfs(grid,i,j-1)

            # for x,y in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
            #     dfs(grid,x,y)


        maxArea = 0
        for i in range(m):
            for j in range(n):
                area = 0
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(grid,i,j))

        return maxArea

#grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[1]]
sol = Solution()
print(sol.maxAreaOfIsland(grid))