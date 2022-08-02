# Given an integer n, return all the structurally unique
# BST's (binary search trees), which has exactly ' \
#    'n nodes of unique values from 1 to n. Return the answer in any order.
#
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) :
        def build(lo, hi):
            if lo > hi:
                return [None]

            allTrees = []
            for i in range(lo, hi + 1):
                leftTrees = build(lo, i - 1)
                rightTrees = build(i + 1, hi)
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees

        return build(1, n) if n else []
