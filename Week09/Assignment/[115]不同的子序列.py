# Given a string S and a string T, count the number of distinct subsequences of 
# S which equals T. 
# 
#  A subsequence of a string is a new string which is formed from the original s
# tring by deleting some (can be none) of the characters without disturbing the re
# lative positions of the remaining characters. (ie, "ACE" is a subsequence of "AB
# CDE" while "AEC" is not). 
# 
#  It's guaranteed the answer fits on a 32-bit signed integer. 
# 
#  Example 1: 
# 
#  
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#  
# 
#  Example 2: 
# 
#  
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
#  
#  Related Topics 字符串 动态规划 
#  👍 233 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(t), len(s)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
