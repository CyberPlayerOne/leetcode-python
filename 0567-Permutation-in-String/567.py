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
            print(f's[{left}:{right}] = {s[left:right]}', valid_chars, len(need),
                  dict(sorted(need.items())),
                  dict(sorted(window.items())), sep='\t')
            c = s[right]
            right += 1

            # 窗口内数据更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid_chars += 1
            # print(f's[{left}:{right}] = {s[left:right]}', valid_chars, len(need), f"{(window[c], need[c]) if c =='e' else ''}")
            # 判断左侧窗口是否需要收缩
            while right - left >= len(t):
                print(f's[{left}:{right}] = {s[left:right]}', valid_chars, len(need),
                      dict(sorted(need.items())),
                      dict(sorted(window.items())), '*', sep='\t')
                # 此处判断是否找到了合法的子串
                if valid_chars == len(need):
                    return True

                d = s[left]
                left += 1

                # 窗口内数据更新
                if d in need:
                    # [重要] 左侧收缩时必须先检查这个，只当window内d符合need中d个数时，才对valid_chars减1.
                    # 如果window[d] > need[d]或者window[d] < need[d]，都不更新valid_chars，否则计数不对。
                    # 比如window[d]本来就小于need[d]，此时valid_chars应该不更新。
                    if window[d] == need[d]:
                        valid_chars -= 1
                    window[d] -= 1

        # 未找到符合条件的子串
        return False


sol = Solution()
assert sol.checkInclusion("ab", "eidboaoo") is False
assert sol.checkInclusion("hello", "ooolleoooleh") is False
assert sol.checkInclusion("trinitrophenylmethylnitramine",
                          "dinitrophenylhydrazinetrinitrophenylmethylnitramine") is True
