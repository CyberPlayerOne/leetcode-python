# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp数组全部初始化为0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # base case
        for i in range(n):
            dp[i][i] = 1
        # 反着遍历保证正确的状态转移
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 状态转移方程
                if s[i] == s[j]:
                    # 他俩一定在最长回文子序列中
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # s[i+1..j]和s[i..j-1] 谁的回文子序列更长？
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # 整个s的最长回文子序列长度
        return dp[0][n - 1]
