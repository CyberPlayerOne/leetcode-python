from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        输入棋盘边长n，返回所有合法的放置
        :param n:
        :return:
        """
        # '.'表示空，'Q'表示皇后，初始化空棋盘

