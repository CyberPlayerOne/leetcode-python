# 322. Coin Change
# https://leetcode.com/problems/coin-change/
# p30, labuladong 的算法小抄
# -----------------------------------------------------------
from typing import List


# 暴力解法 (递归＋自顶向下)
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(n):
            # edge cases
            if n == 0: return 0
            if n < 0: return -1
            # 求最小值，所以初始化为正无穷
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            return res if res != float('INF') else -1

        return dp(amount)


# 带备忘录的递归解法（哈希表＋递归＋自顶向下）
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 备忘录
        memo = dict()

        def dp(n):
            # 查询备忘录，避免重复计算
            if n in memo: return memo[n]

            # edge cases
            if n == 0: return 0
            if n < 0: return -1
            # 求最小值，所以初始化为正无穷
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)


from collections import defaultdict


# DP哈希表的迭代解法（哈希表＋迭代＋自底向上）
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 哈希表的大小为amount + 1， 初始值也为 amount + 1
        dp = defaultdict(lambda: amount + 1)  # dp[i] = x 表⽰， 当⽬标⾦额为 i 时， ⾄少需要 x 枚硬币。
        # edge case
        dp[0] = 0
        for i in range(amount + 1):
            # 内层for在求所有子问题+1的最小值
            for coin in coins:
                # 子问题无解，跳过
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return -1 if dp[amount] == amount + 1 else dp[amount]
