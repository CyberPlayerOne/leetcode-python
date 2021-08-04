# https://leetcode.com/problems/minimum-window-substring/

import sys
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = dict()
        left = 0
        right = 0
        # valid变量表示窗口中满足need条件的字符个数.如果valid和len(need)相等，那么窗口已经满足条件，即完全覆盖t
        valid_chars = 0

        need = collections.Counter(t)


        # 结果
        # 记录最小覆盖子串的起始索引及长度
        start = 0
        min_length = sys.maxsize  # the min min_length found

        while right < len(s):
            print(f's[{left}:{right}] = {s[left:right]}', valid_chars, len(need))
            # c是将要移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1

            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:  # 字符c的个数已被满足
                    valid_chars += 1

            # 判断左侧窗口是否要收缩
            while valid_chars == len(need):  # and left <= right - len(t):
                print(f's[{left}:{right}] = {s[left:right]}', valid_chars, len(need), '*')
                # 在此更新最小覆盖子串
                if right - left < min_length:
                    start = left
                    min_length = right - left

                # d是将要移出的字符
                d = s[left]
                # window左侧右移
                left += 1

                # 进行窗口内数据的更新
                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        valid_chars -= 1

        return '' if min_length == sys.maxsize else s[start:start + min_length]


# Example 1
if __name__ == '__main__':
    sol = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    result = sol.minWindow(s, t)
    print(result)
    assert result == "BANC"

    s = "a"
    t = "a"
    result = sol.minWindow(s, t)
    print(result)
    assert result == "a"

    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    print(f'len(s) = {len(s)}')
    print(f'len(t) = {len(t)}')
    result = sol.minWindow(s, t)
    print(result)
    assert result == "abbbbbcdd"
