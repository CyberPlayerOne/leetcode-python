# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_k = 2
        dp = [[[0 for action in range(2)] for k in range(max_k + 1)] for i in range(n)]
        for i in range(n):
            for k in range(max_k, 0, -1):  # k从max_k递减到1
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = - prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][max_k][0]


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(Solution().maxProfit(prices))
print(Solution().maxProfit(prices) == 6)
prices = [1, 2, 3, 4, 5]
print(Solution().maxProfit(prices))
print(Solution().maxProfit(prices) == 4)
prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices) == 0)
prices = [1]
print(Solution().maxProfit(prices) == 0)
