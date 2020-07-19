# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。 
# 
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。 
# 
#  注意：你不能在买入股票前卖出股票。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        动态规划求解：
        dp[i][0] 表示第i天不持有（卖出）或保持上一天的状态的最大利润，
        dp[i][1] 表示第i天持有的最大利润
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i])
        dp[i][1] = max(dp[i-1][1], - price[i])交易次数只有一次，dp[i][0][0] = 0
        
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0, 0] for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[-1][0]
        """
        # 空间优化
        n = len(prices)
        if n == 0:
            return 0
        pre0_value, pre1_value = 0, -float('INF')
        for i in range(n):
            pre0_value = max(pre0_value, pre1_value + prices[i])
            pre1_value = max(pre1_value, -prices[i])
        return pre0_value

# leetcode submit region end(Prohibit modification and deletion)
