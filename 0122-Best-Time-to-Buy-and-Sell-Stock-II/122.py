# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = - sys.maxsize
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0
