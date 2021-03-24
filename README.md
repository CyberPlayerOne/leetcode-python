# leetcode-python & labuladong 的算法小抄

#### p23 动态规划详解 -> 求最值<p>
1) 关键问题
* 重叠⼦问题、 最优⼦结构、 状态转移⽅程<br/>
2) 解法框架
* 暴力解法 (递归＋自顶向下)<br/>
* 带备忘录的递归解法（哈希表＋递归＋自顶向下）<br/>
* DP哈希表的迭代解法（哈希表＋迭代＋自底向上）<br/>
3) 例题
* 斐波那契数列<br/>
* p30 凑零钱问题 [0322-Coin-Change](0322-Coin-Change/322.py)

#### p37 回溯算法详解 -> 求所有解<p>
回溯算法的决策树遍历框架：
1) 关键问题
* 路径／选择列表／结束条件
2) 解法框架
*  for 循环⾥⾯的递归， 在递归调⽤之前「做选择」 ， 在递归调⽤
之后「撤销选择」<br/>
        for-loop迭代选择:<br/>
            做选择 -> backtrack(路径，选择列表) -> 撤销选择<br/>
3) 例题
* p38 全排列问题 [0046-Permutations](0046-Permutations/46.py)
* p43 N皇后问题 [0051-N-Queens](0051-N-Queens/51.py)

#### p49 BFS 算法框架套路详解 -> 求最近距离、最短路径<p>
写BFS算法要使用队列Queue。<br/>
* p51 二叉树的最小高度 [0111-Minimum-Depth-of-Binary-Tree](0111-Minimum-Depth-of-Binary-Tree/111.py)
* p54 解开密码锁的最小次数 [0752-Open-the-Lock](0752-Open-the-Lock/752.py)
