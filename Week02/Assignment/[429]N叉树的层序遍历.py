# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其层序遍历: 
# 
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#  
# 
#  
# 
#  说明: 
# 
#  
#  树的深度不会超过 1000。 
#  树的节点总数不会超过 5000。 
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result = []
        deque = collections.deque([root])
        while deque:
            level = []
            for i in range(len(deque)):
                node = deque.popleft()
                level.append(node.val)
                deque.extend(node.children)
            result.append(level)
        return result
        
# leetcode submit region end(Prohibit modification and deletion)
