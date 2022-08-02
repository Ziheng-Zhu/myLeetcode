# 给定一个二叉树，检查它是否是镜像对称的。
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def fun(left,right):
            # 如果两边为空
            if not left and not right:
                return True
            # 如果两边一个为空，一个不空
            elif not left or not right:
                return False
            # 如果两边都不空
            else:
                return left.val==right.val \
                       and fun(left.left,right.right) \
                       and fun(left.right,right.left)

        if not root:
            return True
        return fun(root.left,root.right)


# # 下面的代码不是镜像对称，是检查每两个子节点是否对称
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     # 如果是空的树，则对称
    #     if not root:
    #         return True
    #     # 如果是左子树，和右子树都空，则对称
    #     elif not root.left and not root.right:
    #         return True
    #     # 如果是只有一边有，一边无，则不对称
    #     elif not root.left or not root.right:
    #         return False
    #     else:
    #         return self.isSymmetric(root.left) and self.isSymmetric(root.right)
    #
