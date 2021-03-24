# https://leetcode.com/problems/open-the-lock/

from typing import List
from collections import deque


# 向上拨动一次
def plusOne(s: str, j: int) -> str:
    ch = list(s)
    if ch[j] == '9':
        ch[j] = '0'
    else:
        ch[j] = str(int(ch[j]) + 1)
    return ''.join(ch)


# 向下拨动一次
def minusOne(s: str, j: int) -> str:
    ch = list(s)
    if ch[j] == '0':
        ch[j] = '9'
    else:
        ch[j] = str(int(ch[j]) - 1)
    return ''.join(ch)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 记录已经穷举过的密码，防止走回头路
        visited = set()
        q = deque()
        # 从起点开始启动广度优先搜索BFS
        step = 0
        q.append('0000')
        visited.add('0000')

        while len(q) != 0:
            sz = len(q)
            # 将当前队列中的所有节点向周围扩散
            for i in range(sz):
                cur = q.popleft()

                # 判断是否到达终点
                if cur in deadends:
                    continue  # 此路不通
                if cur == target:
                    return step

                # 将一个节点的未遍历相邻节点加入队列
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)

            step += 1

        return -1
