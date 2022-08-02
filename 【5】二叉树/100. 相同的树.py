# 给你两棵二叉树的根节点 p 和q ，编写一个函数来检验这两棵树是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #深度优先搜索:
    # 考虑特殊情况：两个都为空, 返回True.
    # 一个为空，一个不为空，返回False,
    # 两个节点值不同，返回False
    # 两个节点值相同，进入递归：比较左子树和右子树是否相同。
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


    # #广度优先搜索
    # def isSameTree2(self, p: TreeNode, q: TreeNode):
    #     pass

l = TreeNode(0,None,None)
s = TreeNode(1,None,None)
s = TreeNode(2,l,s)
s = TreeNode(3,s,l)
s = TreeNode(4,s,s)

