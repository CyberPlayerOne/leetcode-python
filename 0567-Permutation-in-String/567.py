# https://leetcode.com/problems/permutation-in-string/
import collections


class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:
        window = dict()
        left = 0
        right = 0
        valid_chars = 0

        need = collections.Counter(t)

        while right < len(s):
            # print(f's[{left}:{right}] = {s[left:right]}', valid_chars, len(need), )
            c = s[right]
            right += 1

            # 窗口内数据更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid_chars += 1

            # 判断左侧窗口是否需要收缩
            while right - left >= len(t):
                print(f's[{left}:{right}] = {s[left:right]}', valid_chars, len(need), '*',
                      dict(sorted(need.items())),
                      dict(sorted(window.items())), )
                # 此处判断是否找到了合法的子串
                if valid_chars == len(need):
                    return True

                d = s[left]
                left += 1

                # 窗口内数据更新
                if d in need:
                    window[d] -= 1
                    if window[d] != need[d]:
                        valid_chars -= 1

        # 未找到符合条件的子串
        return False


sol = Solution()
assert sol.checkInclusion("ab", "eidboaoo") is False
assert sol.checkInclusion("trinitrophenylmethylnitramine",
                          "dinitrophenylhydrazinetrinitrophenylmethylnitramine") is True
