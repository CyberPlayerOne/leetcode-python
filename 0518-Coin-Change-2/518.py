# https://leetcode.com/problems/coin-change-2/
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        # base case
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):  # 1 ~ n
            for j in range(1, amount + 1):  # 1 ~ amount
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    assert Solution().change(amount, coins) == 4

    amount = 3
    coins = [2]
    assert Solution().change(amount, coins) == 0

    amount = 10
    coins = [10]
    assert Solution().change(amount, coins) == 1
