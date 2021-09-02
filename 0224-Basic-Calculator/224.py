# https://leetcode.com/problems/basic-calculator/

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: List) -> int:
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
                c = s.pop(0)
                # 如果是数字，连续读入
                if c.isdigit():
                    num = 10 * num + int(c)
                # 遇到左括号，开始递归计算num
                if c == '(':
                    num = helper(s)

                # 如果不是数字，那就大概率是下一个符号，之前的数字和符号要存进stack中
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Python除法 向0取整的写法
                        stack[-1] = int(stack[-1] / float(num))
                    # 更新符号为当前符号，数字清零
                    num = 0
                    sign = c

                # 遇到右括号，返回递归结果
                if c == ')':
                    break
            return sum(stack)

        return helper(list(s))


print(Solution().calculate('1+1'))
print(Solution().calculate('1+3*2'))
print(Solution().calculate('(1+3)*2'))
