# https://leetcode.com/problems/find-all-anagrams-in-a-string/

import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = dict()
        left = 0
        right = 0
        valid_chars = 0

        need = collections.Counter(p)

        # result
        res = []

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid_chars += 1

            while right - left >= len(p):
                if valid_chars == len(need) and right - left == len(p):
                    res += [left]
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid_chars -= 1
                    window[d] -= 1

        return res
