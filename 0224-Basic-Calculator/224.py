# https://leetcode.com/problems/basic-calculator/description/
# 其他：
# https://leetcode.com/problems/basic-calculator-ii/
# https://leetcode.com/problems/basic-calculator-iv/
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: List) -> int:
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
                c = s.pop(0)
                if c.isnumeric():
                    num = 10 * num + int(c)
                # 遇到左括号，开始递归计算num
                if c == '(':
                    num = helper(s)

                if (not c.isnumeric() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Python除法 向0取整的写法
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c

                # 遇到右括号，返回地柜结果
                if c == ')':
                    break
            return sum(stack)

        return helper(list(s))
