# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        # root本身就是一层，depth初始化为1
        depth = 1
        while len(q) != 0:
            sz = len(q)
            pass  # TODO
