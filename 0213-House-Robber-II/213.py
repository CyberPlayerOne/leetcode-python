# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.robRange(nums, 0, n - 2), self.robRange(nums, 1, n - 1))

    def robRange(self, nums: List[int], start: int, end: int) -> int:
        n = len(nums)
        dp_i_1 = 0
        dp_i_2 = 0
        dp_i = 0
        for i in range(end, start - 1, -1):
            dp_i = max(dp_i_1, nums[i] + dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i

        return dp_i


nums = [2, 3, 2]
assert Solution().rob(nums) == 3
nums = [1, 2, 3, 1]
assert Solution().rob(nums) == 4
