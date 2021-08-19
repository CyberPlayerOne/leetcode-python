# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memo = dict()

    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # 利用备忘录消除重叠子问题
        if root in self.memo:
            return self.memo[root]
        # 抢，然后去下下家
        do_it = root.val + (
            0 if root.left is None else self.rob(root.left.left) + self.rob(root.left.right)) + (
                    0 if root.right is None else self.rob(root.right.left) + self.rob(root.right.right)
                )
        # 不抢，然后去下家
        not_do = self.rob(root.left) + self.rob(root.right)
        res = max(do_it, not_do)
        self.memo[root] = res
        return res
