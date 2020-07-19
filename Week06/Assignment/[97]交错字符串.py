# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。 
# 
#  示例 1: 
# 
#  输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false 
#  Related Topics 字符串 动态规划 
#  👍 240 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        dp[i,j]表示s1前i个字符能与s2前i个字符组成s3前i+j个字符
        baseline:dp[0][0] = true
        当i= 0 或 j = 0时，直接拿s2或s1与s3比较，
            dp[0]dp[j] = s2[0-j) == s3[0,j)
            dp[i]dp[0] = s1[0-i) == s3[0,i)
        dp[i][j] = (dp[i-1][j] && s3[i+j-1] == s1[i-1]) || (dp[i][j-1] && s3[i+j-1]==s2[j-1])
        """

        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False

        dp = [[False for i in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True

        for i in range(1, n):
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (
                        dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])
        return dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
