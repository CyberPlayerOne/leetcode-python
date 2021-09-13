# https://leetcode.com/problems/4-keys-keyboard/
# https://cloud.tencent.com/developer/article/1659720
# p181，labuladong的算法小抄

class Solution:
    def maxA(self, N: int) -> int:
        # 对于(n, a_num, copy)这个状态，屏幕上能最终最多能有dp(n, a_num, copy)个A
        def dp(n, a_num, copy):
            # base case
            if n <= 0:
                return a_num
            # 几种选择全试一遍，选择最大的结果
            return max(
                dp(n - 1, a_num + 1, copy),  # A
                dp(n - 1, a_num + copy, copy),  # Ctrl+v
                dp(n - 2, a_num, a_num)  # Ctrl+A, Ctrl+C
            )

        # 可以按N次按键，屏幕和剪切板里都还没有A
        return dp(N, 0, 0)
