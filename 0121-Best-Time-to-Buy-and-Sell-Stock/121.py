# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # k=0,1分别表示：
        # k=0表示无buy和sell；
        # k=1表示有buy；
        dp = [[[0 for action in range(2)] for k in range(2)] for days in range(n)]

        for i in range(n):
            if i - 1 == -1:
                dp[i][1][0] = 0
                dp[i][1][1] = - prices[i]
                continue

            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])

        return dp[n - 1][1][0]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         dp = [[0 for action in range(2)] for days in range(n)]
#
#         for i in range(n):
#             if i - 1 == -1:
#                 dp[i][0] = 0
#                 dp[i][1] = - prices[i]
#                 continue
#
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
#             dp[i][1] = max(dp[i - 1][1], - prices[i])
#
#         return dp[n - 1][0]
