# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 2： 
# 
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rob(self, nums):
        """
        1-动态规划求解(一维)
            1、最优子结构
            dp(n) 表示第i个房子maxValue   dp(n) = max(dp(n-1), dp(n-2) + nums[i])
            2、存储中间状态
            value[i]
            3、递推公式（状态转移方程或递推方程）
            value[i] = max(value[i-1], value[i-2] + nums[i])
            时间复杂度：O（n）

        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        # dp[1]初始化为前2个元素中的最大值，dp从2开始遍历
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
        """
        """
        1-动态规划求解(二维)
            1、最优子结构：dp(n, 0)表示第n个房子不偷， dp(n, 1) 表示第n个房子偷
            dp(n,0) = max(dp(n-1, 1), dp(n-1, 0))
            dp(n,1) = dp(n-1, 0) + nums[n]
            2、存储中间状态： value[i][0/1]
        
        if not nums:
            return 0
        values = [[0, 0] for _ in range(len(nums))]
        values[0][1] = nums[0]
        for i in range(1, len(nums)):
            values[i][0] = max(values[i - 1][1], values[i - 1][0])
            values[i][1] = values[i - 1][0] + nums[i]
        return max(values[-1])
        """

        """
        dp空间优化  在状态转换过程中，实际上只需要存储 i-1 和 i-2 时的状态
        """
        if not nums:
            return 0
        value_1 = 0
        value_2 = 0
        for i in range(len(nums)):
            cur = max(value_1, value_2 + nums[i])
            value_2 = value_1
            value_1 = cur
        return value_1
# leetcode submit region end(Prohibit modification and deletion)
