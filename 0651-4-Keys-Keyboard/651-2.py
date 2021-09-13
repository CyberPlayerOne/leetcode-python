class Solution:
    def maxA(self, N: int) -> int:
        # 备忘录
        memo = dict()

        def dp(n, a_num, copy):
            if n <= 0:
                return a_num
            # 避免计算重复子问题
            if (n, a_num, copy) not in memo:
                memo[(n, a_num, copy)] = max(
                    dp(n - 1, a_num + 1, copy),  # A
                    dp(n - 1, a_num + copy, copy),  # Ctrl+v
                    dp(n - 2, a_num, a_num)  # Ctrl+A, Ctrl+C
                )
            return memo[(n, a_num, copy)]

        return dp(N, 0, 0)
