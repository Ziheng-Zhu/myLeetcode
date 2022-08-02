# 给定一个由 0 和 1 组成的矩阵 mat，
# 请输出一个大小相同的矩阵，
# 其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。

import collections
class Solution:
    # def myupdateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    #     m,n = len(mat),len(mat[0])
    #
    #     # def dfs(i,j):
    #     #
    #     #     if not visited:
    #     #         return 0
    #     #
    #     #     if dfs(i,j)==0:
    #     #         return 0
    #     #
    #     #     for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
    #     #         if 0<=x<m and 0<=y<n:
    #     #             dfs(x,y)
    #     #             visited[x][y]=True
    #     #
    #     #     #return 1+max(dfs(i+1,j),dfs(i-1,j),dfs(i,j+1),dfs(i,j-1))
    #
    #
    #     dismat = [[0]*n for i in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             visited = [ [False] *n for i in range(m)]
    #             if mat[i][j]==0:
    #                 dismat[i][j] == 0
    #             else:
    #                 dismat[i][j] = dfs(i,j)
    #     return  dismat
    #


    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist

