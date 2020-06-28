# 根据一棵树的前序遍历与中序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics 树 深度优先搜索 数组


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left
            root.left = build(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            root.right = build(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        index = {enum: i for i, enum in enumerate(inorder)}
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
# leetcode submit region end(Prohibit modification and deletion)
