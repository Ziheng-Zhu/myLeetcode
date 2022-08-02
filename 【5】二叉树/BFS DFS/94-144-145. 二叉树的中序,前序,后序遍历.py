#给定一个二叉树的根节点 root ，返回它的 中序 遍历。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #中序遍历
    def inorderTraversal(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res


    #前序遍历
    def preorderTraversal(self, root: TreeNode):
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    #后序遍历
    def postorderTraversal(self, root: TreeNode):
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res



l = TreeNode(0,None,None)
s = TreeNode(1,None,None)
s = TreeNode(2,l,s)
s = TreeNode(3,s,l)
s = TreeNode(4,l,s)

sol = Solution()
print('中序遍历',sol.inorderTraversal(s))
print('前序遍历',sol.preorderTraversal(s))
print('后序遍历',sol.postorderTraversal(s))
