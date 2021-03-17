# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# -----------------------------------------------------------
import sys

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self) -> None:
    #     self.ans = -sys.maxsize

    def oneSideMaxWithRoot(self, root: TreeNode) -> int:
        """ max path sum that must includes root node

        Args:
            root (TreeNode): [description]

        Returns:
            int: [description]
        """
        if root is None:
            return -sys.maxsize
        left = max(0, self.oneSideMaxWithRoot(root.left))
        right = max(0, self.oneSideMaxWithRoot(root.right))
        # calculate and update the ans, when calculating oneSideMaxWithRoot.
        self.ans = max(self.ans, left + right + root.val)
        return root.val + max(left, right)

    def maxPathSum(self, root: TreeNode) -> int:
        """max path sum that may or may not include root node

        Args:
            root (TreeNode): [description]

        Returns:
            int: [description]
        """
        if root is None:
            return 0
        self.ans = -sys.maxsize
        self.oneSideMaxWithRoot(root)
        return self.ans
# -----------------------------------------------------------
# https://www.youtube.com/watch?v=9ZNky1wqNUw&ab_channel=HuaHua
# https://www.acwing.com/file_system/file/content/whole/index/content/1753710/
