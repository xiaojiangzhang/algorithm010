# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。 
# 
#  你需要返回给定数组中的重要翻转对的数量。 
# 
#  示例 1: 
# 
#  
# 输入: [1,3,2,3,1]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: [2,4,3,5,1]
# 输出: 3
#  
# 
#  注意: 
# 
#  
#  给定数组的长度不会超过50000。 
#  输入数组中的所有数字都在32位整数的表示范围内。 
#  
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法 
#  👍 115 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    result += 1
        return result

# leetcode submit region end(Prohibit modification and deletion)
