# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = - sys.maxsize
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i] - fee)

        return dp_i_0


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(Solution().maxProfit(prices, fee) == 8)
prices = [1, 3, 7, 5, 10, 3]
fee = 3
print(Solution().maxProfit(prices, fee) == 6)
