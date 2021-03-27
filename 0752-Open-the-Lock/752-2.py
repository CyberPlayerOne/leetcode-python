# https://leetcode.com/problems/open-the-lock/

# 双向BFS (Bi-directional BFS)


from typing import List


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
        # 用集合不用队列queue, 可以快速判断元素是否存在
        q1 = set()
        q2 = set()
        visited = set()

        step = 0
        q1.add('0000')
        q2.add(target)

        while len(q1) != 0 and len(q2) != 0:
            # 哈希集合在遍历的过程中不能修改，用temp存储扩散结果
            temp = set()
            # 将q1中的所有节点向周围扩散
            for cur in q1:
                if cur in deadends:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)

                # 将一个节点的未遍历相邻节点加入集合
                for j in range(4):
                    up = plusOne(cur, j)
                    if up not in visited:
                        temp.add(up)
                    down = minusOne(cur, j)
                    if down not in visited:
                        temp.add(down)

            # 在这里增加步数
            step += 1
            # temp相当于q1
            # 这里交换q1 q2,下一论while就是扩散q2
            q1 = q2
            q2 = temp

        return -1
