class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(i, j):
            # 空串的base case
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                # 找到一个lcs中的元素，继续往前找
                return dp(i - 1, j - 1) + 1
            else:
                # 谁能让lcs最长，就听谁的
                return max(dp(i - 1, j), dp(i, j - 1))

        # i和j初始化为最后一个索引
        return dp(len(text1) - 1, len(text2) - 1)
