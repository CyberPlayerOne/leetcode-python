# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()
        left = 0
        right = 0

        max_len = 0

        while right < len(s):
            d = s[right]
            right += 1
            window[d] = window.get(d, 0) + 1

            while window[d] > 1:
                c = s[left]
                left += 1
                window[c] -= 1

            max_len = max(max_len, right - left)

        return max_len
