# 给定一个无序的整数数组，找到其中最长上升子序列的长度。 
# 
#  示例: 
# 
#  输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
# 
#  说明: 
# 
#  
#  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
#  你算法的时间复杂度应该为 O(n2) 。 
#  
# 
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
#  Related Topics 二分查找 动态规划 
#  👍 889 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i]表示前i个数字最大上升子序列长度
        nums[i]>nums[i-1] 时，dp[i] = dp[i-1] + 1
        """
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

# leetcode submit region end(Prohibit modification and deletion)
