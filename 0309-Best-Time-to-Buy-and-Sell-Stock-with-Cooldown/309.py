# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -sys.maxsize
        dp_pre_0 = 0  # 代表dp[i-2][0]
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp

        return dp_i_0


prices = [1,2,3,0,2]
print(Solution().maxProfit(prices))