# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 深度优先
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node):
            if not node:
                return float("inf")
            elif not node.left  and not node.right:
                return 1
            return min(dfs(node.left),dfs(node.right))+1
        return dfs(root)

    # 广度优先
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 1
        while queue:
            for i in range(len(queue)):
                # queue保存同一层所有的节点
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        return depth
