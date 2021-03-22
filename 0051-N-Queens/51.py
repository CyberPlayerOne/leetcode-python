# https://leetcode.com/problems/n-queens/
from typing import List
import copy


class Solution:

    def __init__(self):
        self.res = list()  # List[List[str]]

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        输入棋盘边长n，返回所有合法的放置
        :param n:
        :return:
        """
        # '.'表示空，'Q'表示皇后，初始化空棋盘
        board = [['.'] * n for _ in range(n)]  # To create n different sub lists
        self.backtrack(board, 0)
        return [[''.join(line) for line in b] for b in self.res]

    def backtrack(self, board: List[List[str]], row: int):
        """
        路径：board中小于row的那些行都已经成功放置了皇后
        选择列表：第row行的所有列都是放置皇后的选择
        结束条件：row超过board的最后一行
        :param board:
        :param row:
        :return:
        """
        # 触发结束条件
        if row == len(board):
            self.res.append(copy.deepcopy(board))
            return

        n = len(board[row])
        for col in range(n):
            # 排除不合法选择
            if not self.isValid(board, row, col):
                continue
            # 做选择
            board[row][col] = 'Q'
            # 进入下一行决策
            self.backtrack(board, row + 1)
            # 撤销选择
            board[row][col] = '.'

    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        """
        是否可以在board[row][col]放置皇后？
        :param board:
        :param row:
        :param col:
        :return:
        """
        n = len(board)
        # 检查列是否有皇后互相冲突
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        # 检查左上方斜线是否有皇后互相冲突
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        # 检查右上方斜线是否有皇后互相冲突
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
            if board[i][j] == 'Q':
                return False

        return True

# print(Solution().solveNQueens(4))
