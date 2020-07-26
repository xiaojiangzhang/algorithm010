# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 
# 的朋友。所谓的朋友圈，是指所有朋友的集合。 
# 
#  给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你
# 必须输出所有学生中的已知的朋友圈总数。 
# 
#  示例 1: 
# 
#  
# 输入: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
#  
# 
#  注意： 
# 
#  
#  N 在[1,200]的范围内。 
#  对于所有学生，有M[i][i] = 1。 
#  如果有M[i][j] = 1，则有M[j][i] = 1。 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def union(i, j):
            pi = find(i)
            pj = find(j)
            self.parent[pi] = pj

        def find(i):
            root = i
            while self.parent[root] != root:
                root = self.parent[root]

            while self.parent[i] != i:
                x = i
                i = self.parent[i]
                self.parent[x] = root
            return root

        # 并查集求解
        # 初始化并查集
        n = len(M)
        self.parent = [i for i in range(n)]
        for i in range(n):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    union(i, j)
        return len(set([find(i) for i in range(n)]))

    # dfs实现
    # visited, count, m, n = [0 for _ in range(len(M))], 0, len(M), len(M[0])
    #
    # def dfs(i, visited):
    #     for j in range(n):
    #         if M[i][j] == 1 and not visited[j]:
    #             visited[j] = 1
    #             dfs(j, visited)
    #
    # for i in range(m):
    #     if not visited[i]:
    #         count += 1
    #         dfs(i, visited)
    # return count

# leetcode submit region end(Prohibit modification and deletion)
