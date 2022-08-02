

class Solution:
    def numDistinctIslands(self, grid):
        m, n = len(grid), len(grid[0])
        # sb 是记录dfs函数遍历的顺序，遍历的顺序决定了岛屿的形状
        # dfs 就是遍历的方向，组成了sb
        # sb 需要用list来记录，每次添加转化成字符串的str,
        # 这样sb就是一个字符串序列，方便用join进行转化

        def dfs(grid,i,j,sb,dir):
            if i<0 or j<0 or i>= m or j>= n or grid[i][j]==0:
                return
            grid[i][j]=0
            sb.append(str(dir))
            dfs(grid,i-1,j,sb,1)
            dfs(grid,i+1,j,sb,2)
            dfs(grid,i,j-1,sb,3)
            dfs(grid,i,j+1,sb,4)
            #sb.append(str(-dir))

        # islands 是一个集合，记录岛屿的数量
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    s = []
                    # 初始方向可以随便写，不影响正确性
                    dfs(grid,i,j,s,0)
                    # 添加转化成方向序列的岛屿，用set来记录，set的大小就是不同岛屿数量
                    islands.add(''.join(s))
                    print(islands)
        return len(islands)


#grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
#grid = [[1,1],[0,0]]
#grid = [[0,1,1,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
grid = [[0,1,1,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
sol = Solution()
print(sol.numDistinctIslands(grid))