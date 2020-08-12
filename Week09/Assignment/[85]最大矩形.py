# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  示例: 
# 
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6 
#  Related Topics 栈 数组 哈希表 动态规划 
#  👍 539 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxArea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxArea = max(maxArea, width * (i - k + 1))
        return maxArea

# leetcode submit region end(Prohibit modification and deletion)
