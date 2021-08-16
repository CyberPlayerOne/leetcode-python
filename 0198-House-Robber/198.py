# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    memo = []

    def rob(self, nums: List[int]) -> int:
        # 初始化备忘录
        self.memo = [-1 for _ in range(len(nums))]
        # 强盗从第0间房子开始抢劫
        return self.dp(nums, 0)

    # 返回dp[?,start]能抢到的最大值
    def dp(self, nums: List[int], start: int) -> int:
        if start >= len(nums):
            return 0
        # 避免重复计算
        if self.memo[start] != -1:
            return self.memo[start]

        res = max(self.dp(nums, start + 1), nums[start] + self.dp(nums, start + 2))
        # 记入备忘录
        self.memo[start] = res
        return res


nums = [1, 2, 3, 1]
assert Solution().rob(nums) == 4

nums = [2,7,9,3,1]
assert Solution().rob(nums) == 12
