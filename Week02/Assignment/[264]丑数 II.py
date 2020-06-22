# 编写一个程序，找出第 n 个丑数。 
# 
#  丑数就是质因数只包含 2, 3, 5 的正整数。 
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
#  Related Topics 堆 数学 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n)]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min([dp[p2] * 2, dp[p3] * 3, dp[p5] * 5])
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1

        return dp[n-1]

# leetcode submit region end(Prohibit modification and deletion)
