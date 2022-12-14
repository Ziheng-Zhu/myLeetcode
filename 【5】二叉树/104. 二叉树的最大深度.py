# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。

#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 1
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

l = TreeNode(0,None,None)
s = TreeNode(1,None,None)
s = TreeNode(2,l,s)
s = TreeNode(3,s,l)
s = TreeNode(4,s,s)

sol = Solution()
print(sol.maxDepth(s))
