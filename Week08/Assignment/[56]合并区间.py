# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  示例 1: 
# 
#  输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
#  Related Topics 排序 数组 
#  👍 525 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals = sorted(intervals)
        merge = [intervals[0]]
        # print(merge)
        for start, end in intervals:
            if start > merge[-1][1]:
                print([start, end])
                merge.append([start, end])
            elif end > merge[-1][1]:
                merge[-1][1] = end
        return merge
        # leetcode submit region end(Prohibit modification and deletion)
