
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # 102:层序遍历：给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
    def levelOrder(self, root: TreeNode):
        # queue 用来存放节点
        # res 用来保存按照层序遍历的节点值
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            # 把当前层queue的结点值插入队列
            res.append([node.val for node in queue])
            # 遍历当前层的每个结点的左右子节点，入队列，
            # 把queue列表更新成当前层的子节点
            ll = []
            for node in queue:
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue = ll
        return res

    # 103：二叉树的锯齿形层序遍历
    # 给定一个二叉树，返回其节点值的锯齿形层序遍历。
    # （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
    def zigzagLevelOrder(self, root: TreeNode):
        # queue 用来存放节点
        # res 用来保存按照层序遍历的节点值
        if not root:
            return []
        queue = [root]
        res = []
        is_even_level = True
        while queue:
            # 把当前层queue的结点值插入队列
            if is_even_level:
                res.append([node.val for node in queue])
            else:
                res.append([node.val for node in queue][::-1])
            # 遍历当前层的每个结点的左右子节点，入队列，
            # 把queue列表更新成当前层的子节点
            ll = []
            for node in queue:
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue = ll
            is_even_level = not is_even_level
        return res

    # 107: 给定一个二叉树，返回其节点值自底向上的层序遍历;
    # 即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历
    def levelOrderBottom(self, root: TreeNode):
        # 只需对levelOrder的表倒叙即可
        res = self.levelOrder(root)
        return res[::-1]

    # 199：给定一个二叉树的 根节点 root，想象自己站在它的右侧，
    # 按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
    def rightSideView(self, root: TreeNode):
        # queue 用来存放节点
        # res 用来保存按照层序遍历的节点值
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            # 把当前层queue的结点值插入队列
            res.append([node.val for node in queue][-1])
            # 遍历当前层的每个结点的左右子节点，入队列，
            # 把queue列表更新成当前层的子节点
            ll = []
            for node in queue:
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue = ll
        return res


l = TreeNode(0,None,None)
s = TreeNode(1,None,None)
s = TreeNode(2,l,s)
s = TreeNode(3,s,l)
s = TreeNode(4,s,s)

sol = Solution()
print(sol.levelOrder(s))
print(sol.zigzagLevelOrder(s))
print(sol.levelOrderBottom(s))
print(sol.rightSideView(s))