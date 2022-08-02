# 给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，
# 请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，
# 并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。

class Solution:

    # # 广度优先
    # def numIslands(self, grid) -> int:
    #


    # 深度优先
    def numIslands(self, grid) -> int:

        res = 0
        m,n = len(grid),len(grid[0])

        # 从 (i,j) 开始，将与之相邻的 ‘1’ 都变为 ‘0’
        def dfs(grid,i,j):

            if i<0 or j< 0 or i>=m or j>=n:
                return
            if grid[i][j]== '0':
                return
            grid[i][j] = '0'
            # (i,j) 的上下左右
            for x,y in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                # 只对在边界上的 坐标进行操作
                # if 0<=x<m and 0<=y<n and grid[x][y]=='1':
                    dfs(grid,x,y)


        for i in range(m):
            for j in range(n):
                # 如果发现了一个岛屿，岛屿数量+1
                # 并且把岛屿给淹了
                if grid[i][j] == '1':
                    res +=1
                    dfs(grid,i,j)
        return res


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
sol = Solution()
print(sol.numIslands(grid))