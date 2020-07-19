# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pre_max = nums[0]
        pre_min = nums[0]
        res = nums[0]
        for i in range(1, n):
            cur_max = max(pre_max * nums[i], pre_min * nums[i], nums[i])
            cur_min = min(pre_max * nums[i], pre_min * nums[i], nums[i])
            res = max(cur_max, res)
            pre_max = cur_max
            pre_min = cur_min

        return res

# leetcode submit region end(Prohibit modification and deletion)
