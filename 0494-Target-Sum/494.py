# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    def __init__(self):
        # memo
        self.memo = dict()

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            return self.dp(nums, 0, target)

    def dp(self, nums: List[int], i: int, rest: int):
        # print(f'i={i}')
        # base case
        if i == len(nums):
            if rest == 0:
                return 1
            else:
                return 0

        # 把他俩转成字符串才能作为哈希表的键
        key = f'{i},{rest}'
        # 避免重复计算
        if key in self.memo:
            return self.memo[key]
        # 穷举
        result = self.dp(nums, i + 1, rest - nums[i]) + self.dp(nums, i + 1, rest + nums[i])  # +nums[i]和-nums[i]的各自情况
        # 记入memo
        self.memo[key] = result
        return result


print(Solution().findTargetSumWays([1, 0], 1))
print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
