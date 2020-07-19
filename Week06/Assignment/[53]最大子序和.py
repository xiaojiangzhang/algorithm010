# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 简单dp求解
        # dp = nums
        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i - 1] + dp[i], dp[i])
        # return max(dp)

        # 分治求解 最大子序列和只有三种情况，分别是在中心点左侧、中心点右侧、跨中心点

        n = len(nums)
        # 递归终止条件 当序列个数为1时直接返回
        if n == 1:
            return nums[0]
        # 分别递归计算左半边和右半边最大子序和
        else:
            left = self.maxSubArray(nums[0:len(nums) // 2])
            right = self.maxSubArray(nums[len(nums) // 2:])
        # 计算中间的最大自序和，从右到左计算左边的最大子序和，从作到右计算右边的最大子序和，再进行相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for j in range(len(nums) // 2, len(nums)):
            tmp += nums[j]
            max_r = max(tmp, max_r)
        return max(left, right, max_r + max_l)
    # leetcode submit region end(Prohibit modification and deletion)
