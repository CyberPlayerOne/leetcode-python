# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return len(intervals) - self.intervalSchedule(intervals)

    # Maximum number of non-overlapped intervals
    def intervalSchedule(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        # 按end升序排序
        intervals = sorted(intervals, key=lambda i: i[1])
        # 至少有一个区间不相交
        count = 1
        # 排序后，第一个区间就是ｘ
        x_end = intervals[0][1]
        for interval in intervals:
            start = interval[0]
            if start >= x_end:
                # 找到下一个选择的区间了
                count += 1
                x_end = interval[1]

        return count
