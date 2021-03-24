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
            sz = len(q)  # 二叉树中第depth层的节点个数
            # 将当前队列中的所有节点向四周扩散
            for i in range(sz):
                cur = q.popleft()
                # 判断是否到达终点
                if cur.left is None and cur.right is None:
                    return depth
                # 将cur的相邻节点left和right加入队列
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            # 这里增加步数
            depth += 1

        return depth
