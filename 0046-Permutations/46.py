# https://leetcode.com/problems/permutations/
from typing import List
import copy


class Solution:
    def __init__(self):
        self.res = list()  # List[List[int]]

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        路径：记录在track中
        选择列表：nums中不存在于track的那些元素
        结束条件：nums中的元素全都在track中出现
        :param nums:
        :return:
        """
        track = list()  # List[int]
        self.backtrack(nums, track)
        return self.res

    def backtrack(self, nums: List[int], track: List[int]):
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(copy.deepcopy(track))  # Needs to create a new list otherwise it's merely a ref
            # print(track, self.res)
            return

        for i in range(len(nums)):
            # 排除不合法的选择
            if nums[i] in track:
                continue
            # 做选择i
            track.append(nums[i])
            # 进入下一层决策树
            self.backtrack(nums, track)
            # 取消选择i，之后在下一次iteration中尝试选择i+1在此位置
            track.pop()

# print(Solution().permute([1, 2, 3]))
