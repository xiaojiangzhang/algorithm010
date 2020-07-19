# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
#  Related Topics 字符串 动态规划 
#  👍 441 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        # 定义dp数组，dp[i]表示以s[0...i]所能构成的解码总数
        dp = [0 for _ in range(n)]
        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            num = 10 * (ord(s[i - 1]) - ord('0')) + (ord(s[i]) - ord('0'))
            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[n - 1]
        # leetcode submit region end(Prohibit modification and deletion)
