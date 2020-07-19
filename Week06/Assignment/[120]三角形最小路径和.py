# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。 
# 
#  相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。 
# 
#  
# 
#  例如，给定三角形： 
# 
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
# 
#  
# 
#  说明： 
# 
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # ---递归求解，自顶向下  ----纯递归超时，增加记忆搜索
        # n = len(triangle)
        # memo = [[float('inf')] * n for i in range(n)]
        #
        # def helpers(level, position):
        #     if memo[level][position] != float("INF"):
        #         return memo[level][position]
        #     if level == len(triangle) - 1:
        #         return triangle[level][position]
        #
        #     left = helpers(level + 1, position)
        #     right = helpers(level + 1, position + 1)
        #     memo[level][position] = min(left, right) + triangle[level][position]
        #     return memo[level][position]
        #
        # return helpers(0, 0)
        # --动态规划求解: 状态定义：dp[i][j]表示三角形中第i行第j列的最短路径，dp[i][i] = min(dp[i-1][j-1], dp[i-1][j])
        # n = len(triangle)
        # dp = [[0] * n for i in range(n)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, n):
        #     dp[i][0] = dp[i - 1][0] + triangle[i][0]
        #     for j in range(1, i):
        #         dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        #     dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        # return min(dp[-1])
        # --动态规划自底向上求解
        # m = len(triangle)
        # dp = [[0] * m for i in range(m)]
        # dp[-1] = triangle[-1]
        # for i in range(m - 2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        # return dp[0][0]

        # --优化DP 使用triangle底边大小存储状态
        if not triangle:
            return
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j + 1], dp[j]) + triangle[i][j]
        print(dp)
        return dp[0]

# leetcode submit region end(Prohibit modification and deletion)
