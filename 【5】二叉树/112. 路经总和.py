# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，
# 判断该树中是否存在 根节点到叶子节点 的路径，
# 这条路径上所有节点值相加等于目标和 targetSum 。
#
# 叶子节点 是指没有子节点的节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 写的太复杂了...但是是全部自己写的
    def hasPathSum(self, root, targetSum: int) -> bool:
        # 如果是空节点，连值都没有，肯定不对
        if not root:
            return False
        # 如果root没有子节点
        if not root.left and not root.right:
            return targetSum == root.val
            # 太冗余了，一行代码就行其实
            # if root.val == targetSum:
            #     return True
            # else:
            #     return False
        # 这个条件其实没必要写，包含在了最后一个条件里
        # if root.left and not root.right:
        #     return self.hasPathSum(root.left, targetSum-root.val)
        # if root.right and not root.left:
        #     return self.hasPathSum(root.right,targetSum-root.val)

        # 如果 root 两边至少有一边有节点
        if root.right or root.left:
            return self.hasPathSum(root.left,targetSum-root.val) \
                   or self.hasPathSum(root.right,targetSum-root.val)