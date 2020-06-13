//假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
// 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
// 注意：给定 n 是一个正整数。
// 示例 1：
// 输入： 2
//输出： 2
//解释： 有两种方法可以爬到楼顶。
//1.  1 阶 + 1 阶
//2.  2 阶 
// 示例 2：
// 输入： 3
//输出： 3
//解释： 有三种方法可以爬到楼顶。
//1.  1 阶 + 1 阶 + 1 阶
//2.  1 阶 + 2 阶
//3.  2 阶 + 1 阶
// 
// Related Topics 动态规划


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    /*
    1、暴力递归：
        n>2时 ：f(n) = f(n-1)+f(n-2)
        时间复杂度：O（2^N）
        空间复杂度：O（N）
    2、带优化的递归：
        递归过程对递归树进行记录，避免重复计算
        时间复杂度：O（N）
        空间复杂度：O（N）
    3、动态规划：
        使用dp数组记录步数，状态定义为dp[i]表示爬i层最多有多少种方法，状态转移为dp[i] = dp[i-1] + dp[i-2]
        时间复杂度：O(N)
        空间复杂度：O(N)
    3、递推：
        在求解过程中，类似于斐波拉契数列，实际上只用到了n-1和n-2时的状态，只需要记录这两个状态并且进行更新即可。
        时间复杂度：O（N）
        空间复杂度：O（1）
    * */
    public int climbStairs1(int n) {
        if (n <= 2) {
            return n;
        }
        return climbStairs(n - 1) + climbStairs(n - 2);
    }

    public int climbStairs2(int n) {
        int[] memo = new int[n + 1];
        Arrays.fill(memo, 0);
        return climb(n, memo);
    }

    public int climb(int n, int[] memo) {
        if (n <= 2) {
            return n;
        }
        if (memo[n] != 0) {
            return memo[n];
        }
        memo[n] = climb(n - 1, memo) + climb(n - 2, memo);
        return memo[n];
    }

    public int climbStairs3(int n) {
        if (n <= 2) {
            return n;
        }
        int[] dp = new int[n + 1];

        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        int pos1 = 1;
        int pos2 = 2;

        for (int i = 3; i <= n; i++) {
            int temp = pos1 + pos2;
            pos1 = pos2;
            pos2 = temp;
        }
        return pos2;

    }


}
//leetcode submit region end(Prohibit modification and deletion)
