# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        M = len(needle)
        N = len(haystack)
        if M == 0:
            return 0
        for i in range(N - M + 1):
            # print(f'\n i={i}->', end='')
            j = 0
            for j in range(M):
                # print(j, end='')
                if needle[j] != haystack[i + j]:
                    break
            # needle全部匹配时
            if needle[j] == haystack[i + j] and j == M - 1:
                return i
        # haystack中不存在needle子串
        return -1


print('\n', Solution().strStr('abc', 'c'))
