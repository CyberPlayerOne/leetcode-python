# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points = sorted(points, key=lambda p: p[1])
        count = 1
        prev_end = points[0][1]
        for point in points:
            curr_start = point[0]
            if curr_start > prev_end:
                count += 1
                prev_end = point[1]
        return count
