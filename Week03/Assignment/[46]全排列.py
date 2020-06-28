# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        track = []
        res = []

        def backtrack(nums, track):
            if len(track) == len(nums):
                # print(track)
                res.append(track[:])
                return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                backtrack(nums, track)
                track.pop()

        backtrack(nums, track)
        return res
# leetcode submit region end(Prohibit modification and deletion)
