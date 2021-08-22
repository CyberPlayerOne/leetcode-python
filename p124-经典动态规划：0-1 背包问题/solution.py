from typing import List


class Solution:
    def knapsack(self, w: int, n: int, wt: List[int], val: List[int]) -> int:
        dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
        for _i in range(1, n + 1):
            for _w in range(1, w + 1):
                if _w - wt[_i - 1] < 0:
                    # 当前背包量装不下，只能选择不装入背包
                    dp[_i][_w] = dp[_i - 1][_w]
                else:
                    # 装入或者不装入背包，择优
                    dp[_i][_w] = max(dp[_i - 1][_w - wt[_i - 1]] + val[_i - 1], dp[_i - 1][_w])

        return dp[n][w]
