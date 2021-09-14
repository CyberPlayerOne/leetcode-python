# leetcode-python </br>& </br> labuladong的算法小抄

#### p23 动态规划详解 -> <u>求最值</u><p>

动态规划问题的⼀般形式就是求最值。 动态规划其实是运筹学的⼀种<u>最优化⽅法</u>， 只不过在计算机问题上应⽤⽐较多， ⽐如说让你求<u>最⻓递增⼦序列</u>呀， <u>最⼩编辑距离</u>呀等等。

1) 关键问题

* 重叠⼦问题、 最优⼦结构、 状态转移⽅程<br/>

2) 解法框架

* 暴力解法 (递归＋自顶向下)<br/>
* 带备忘录的递归解法（哈希表＋递归＋自顶向下）<br/>
* DP哈希表的迭代解法（哈希表＋迭代＋自底向上）<br/>

3) 例题

* 斐波那契数列<br/>
* p30 凑零钱问题 [0322-Coin-Change](0322-Coin-Change/322.py)

#### p37 回溯算法详解 -> <u>求所有解，或所有解的总数</u><p>

解决⼀个回溯问题， 实际上就是⼀个决策树的遍历过程。 回溯算法的决策树遍历框架：

1) 关键问题

* 路径／选择列表／结束条件

2) 解法框架

* for 循环⾥⾯的递归， 在递归调⽤之前「做选择」 ， 在递归调⽤ 之后「撤销选择」<br/>
  for-loop迭代选择:<br/>
  做选择 -> backtrack(路径，选择列表) -> 撤销选择<br/>

3) 例题

* p38 全排列问题 [0046-Permutations](0046-Permutations/46.py)
* p43 N皇后问题 [0051-N-Queens](0051-N-Queens/51.py)

#### p49 BFS 算法框架套路详解 -> <u>求最近距离、最短路径</u><p>

写BFS算法要使用队列Queue。<br/>

* p51 二叉树的最小高度 [0111-Minimum-Depth-of-Binary-Tree](0111-Minimum-Depth-of-Binary-Tree/111.py)
* p54 解开密码锁的最小次数 [0752-Open-the-Lock](0752-Open-the-Lock/752.py) <br/>
  p59 双向BFS优化 [0752-Open-the-Lock](0752-Open-the-Lock/752-2.py) <br/>

#### p63 ⼆分查找详解 -> <u>TODO</u><p>

p71

#### p80 滑动窗⼝算法框架 -> <u>字符串内移动匹配的问题</u><p>

参见：我写了套框架，把滑动窗口算法变成了默写题 - labuladong[重要].pdf

* 最小覆盖子串 [0076-Minimum-Window-Substring](0076-Minimum-Window-Substring/76.py)
* 字符串排列 [0567-Permutation-in-String](0567-Permutation-in-String/567.py): Match & Permutation这种题，考虑对比dict字母计数（collections.Counter(t)）。
* 找所有字母异位词 [0438-Find-All-Anagrams-in-a-String](0438-Find-All-Anagrams-in-a-String/438.py)
* 最长无重复子串 [0003-Longest-Substring-Without-Repeating-Characters](0003-Longest-Substring-Without-Repeating-Characters/3.py)

#### p84 团灭 LeetCode 股票买卖问题 -> <u>动态规划dp</u><p>

参见： #labuladong 公众号：LeetCode买卖股票问题汇总

* [0121-Best-Time-to-Buy-and-Sell-Stock](0121-Best-Time-to-Buy-and-Sell-Stock/121.py)
* [0122-Best-Time-to-Buy-and-Sell-Stock-II](0122-Best-Time-to-Buy-and-Sell-Stock-II/122.py)
* [0309-Best-Time-to-Buy-and-Sell-Stock-with-Cooldown](0309-Best-Time-to-Buy-and-Sell-Stock-with-Cooldown/309.py)
* [0714-Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee](0714-Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee/714.py)
* [0123-Best-Time-to-Buy-and-Sell-Stock-III](0123-Best-Time-to-Buy-and-Sell-Stock-III/123.py)
* [0188-Best-Time-to-Buy-and-Sell-Stock-IV](0188-Best-Time-to-Buy-and-Sell-Stock-IV/188.py)

#### p97 团灭 LeetCode 打家劫舍问题 -> <u>动态规划dp</u><p>

参见：经典动态规划：打家劫舍系列问题.pdf

* [0198-House-Robber](0198-House-Robber/198.py)
* [0213-House-Robber-II](0213-House-Robber-II/213.py)
* [0337-House-Robber-III](0337-House-Robber-III/337.py)

#### p99, p119 回溯算法和动态规划， 谁是谁爹？ -> <u>?</u><p>

参见：动态规划和回溯算法到底谁是谁爹？ - labuladong 的算法小抄.pdf

* [0494-Target-Sum](0494-Target-Sum/494.py)
* [0001-Two-Sum](0001-Two-Sum/1.py) #TODO
* [0015-3Sum](0015-3Sum/15.py) #TODO
* [0018-4Sum](0018-4Sum/18.py) #TODO

#### p101 经典动态规划问题： ⾼楼扔鸡蛋 -> <u>TODO</u><p>

* [0887-Super-Egg-Drop](0887-Super-Egg-Drop/887.py) #TODO

#### p140 经典动态规划问题： ⾼楼扔鸡蛋（进阶） -> <u>TODO</u><p>

#### p123 动态规划之背包问题 -> <u></u><p>

参见：#labuladong 公众号：背包类型问题/1 - 经典动态规划：0-1 背包问题.pdf

* [p124-经典动态规划：0-1背包问题](p124-经典动态规划：0-1背包问题/solution.py)

#### p104 背包问题变体之⼦集分割 -> <u>DP</u><p>

* [0416-Partition-Equal-Subset-Sum](0416-Partition-Equal-Subset-Sum/416.py)

#### p110 背包问题之零钱兑换 -> <u>DP</u><p>

* [0518-Coin-Change-2](0518-Coin-Change-2/518.py)

#### p115 拆解复杂问题： 实现计算器 -> <u></u><p>

参见：#labuladong 公众号：如何拆解复杂问题：实现一个计算器

* [0224-Basic-Calculator](0224-Basic-Calculator/224.py)
* [0227-Basic-Calculator-II](0227-Basic-Calculator-II/227.py) #TODO
* [0770-Basic-Calculator-IV](0770-Basic-Calculator-IV/770.py) #TODO

#### p117 动态规划系列 -> <u></u><p>

参见：#labuladong 公众号：动态规划答疑篇

#### p122 动态规划设计： 最⻓递增⼦序列 -> <u></u><p>

参见：#labuladong 公众号：动态规划设计之最⻓递增⼦序列

* [0300-Longest-Increasing-Subsequence](0300-Longest-Increasing-Subsequence/300-1.py)

#### p127 编辑距离 -> <u>#TODO</u><p>

* [0072-Edit-Distance](0072-Edit-Distance/72.py) #TODO

#### p140 经典动态规划问题： ⾼楼扔鸡蛋（进阶） -> <u>#TODO</u><p>

参见：#labuladong 公众号：经典动态规划：高楼扔鸡蛋（进阶篇）

#### p152 经典动态规划： 戳⽓球 -> <u>Hard</u> TODO<p>

参见：#labuladong 公众号：经典动态规划：戳气球问题

* [0312-Burst-Balloons](0312-Burst-Balloons/312.py) #TODO

#### p155 最⻓公共⼦序列 -> <u></u><p>

* [1143-Longest-Common-Subsequence](1143-Longest-Common-Subsequence/1143-dp-table.py)

#### p162 动态规划之⼦序列问题解题模板 -> <u></u><p>

参见：#labuladong 公众号：动态规划设计之最⻓递增⼦序列

* [0516-Longest-Palindromic-Subsequence](0516-Longest-Palindromic-Subsequence/516.py)

#### p164 动态规划之博弈问题 -> <u>TODO</u><p>

#### p173 动态规划之正则表达 -> <u>TODO</u><p>

[0010-Regular-Expression-Matching](0010-Regular-Expression-Matching/10.py)

#### p181 动态规划之四键键盘 -> <u>动态规划：不同的状态设计</u><p>

[0651-4-Keys-Keyboard](0651-4-Keys-Keyboard/)

#### p188 动态规划之KMP字符匹配算法 -> <u>TODO</u><p>

[0028-Implement-strStr()](0028-Implement-strStr())

参见 [动态规划之 KMP 算法详解](https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484731&idx=2&sn=d9d6b24c7f94d5e43e08666e82251984)

p193