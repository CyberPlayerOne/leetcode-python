# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        # 和为奇数时，不可能划分成两个和相等的集合
        if _sum % 2 != 0:
            return False
        n = len(nums)
        _sum = int(_sum / 2)
        dp = [[False for _ in range(_sum + 1)] for _ in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, _sum + 1):
                if j - nums[i - 1] < 0:
                    # 背包容量不足，不能装入第i个物品
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 装入或不装入背包
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][_sum]


nums = [1, 5, 11, 5]
assert Solution().canPartition(nums) is True
