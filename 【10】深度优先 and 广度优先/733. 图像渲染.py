# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，
# 数值在 0 到 65535 之间。
#
# 给你一个坐标(sr, sc)表示图像渲染开始的像素值（行 ，列）
# 和一个新的颜色值newColor，让你重新上色这幅图像。
#
# 为了完成上色工作，从初始坐标开始，
# 记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，
# 接着再记录这四个方向上符合条件的像素点
# 与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，
# 重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
#
# 最后返回经过上色渲染后的图像。


class Solution:
    # 广度优先
    def floodFillBFS(self, image, sr: int, sc: int, newColor: int):
        originalColor = image[sr][sc]
        if originalColor == newColor:
            return image
        m,n = len(image),len(image[0])
        que = [(sr,sc)]
        while que:
            x,y = que.pop(0)
            for mx,my in [(x-1,y),(x+1,y),
                          (x,y-1),(x,y+1)]:
                if 0<=mx<n and 0<= my<m and\
                        image[mx][my] == originalColor:
                    que.append((mx,my))
                    image[mx][my] = newColor
        return image

    # 深度优先
    def floodFillDFS(self, image, sr: int, sc: int, newColor: int):
        m, n = len(image), len(image[0])
        originalColor = image[sr][sc]

        def dfs(r,c):
            if image[x][y] == originalColor:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y),
                               (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and \
                            image[mx][my] == originalColor:
                        dfs(mx,my)
        if originalColor!= newColor:
            dsf(sr,sc)
        # def dfs(r,c):
        #     if r == m or c == n or r<0 or c<0:
        #         return
        #     elif image[r][c]!=originalColor:
        #         return
        #     elif image[r][c] == newColor:
        #         return
        #     else:
        #         image[r][c] = newColor
        #         dfs(r-1,c)
        #         dfs(r,c-1)
        #         dfs(r+1,c)
        #         dfs(r,c+1)
        # dfs(sr,sc)
        return image

image = [[0,0,0],[0,1,1]]
sol = Solution()
print(sol.floodFillBFS(image,1,1,1))
print(sol.floodFillDFS(image,1,1,1))