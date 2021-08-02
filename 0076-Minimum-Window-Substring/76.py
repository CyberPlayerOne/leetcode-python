# https://leetcode.com/problems/minimum-window-substring/

import sys
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = collections.OrderedDict()
        need = collections.Counter(t)

        left = 0
        right = 0
        # valid变量表示窗口中满足need条件的字符个数.如果valid和len(need)相等，那么窗口已经满足条件，即玩全覆盖t
        valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = sys.maxsize
        while right < len(s):
            # c是将要移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:  # 字符c的个数已被满足
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在此更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left

                # d是将要移出的字符
                d = s[left]
                # 左侧右移
                left += 1
                # 进行窗口内数据的更新
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return '' if length == sys.maxsize else s[start:start + length]
