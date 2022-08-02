# 给你一个整数数组 nums ，其中元素已经按 升序 排列，
# 请你将其转换为一棵 高度平衡 二叉搜索树。
#
# 高度平衡 二叉树是一棵满足
# 「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def helper(left,right):
            if left>right:
                return None
            # 总是选择中间按位置左边的数字作为根节点
            mid = (left + right)//2
            root = TreeNode(nums[mid])
            root.left = helper(left,mid-1)
            root.right = helper(mid+1,right)
            return root
        return helper(0,len(nums)-1)

nums = [-10,-3,0,5,9]
sol = Solution()


