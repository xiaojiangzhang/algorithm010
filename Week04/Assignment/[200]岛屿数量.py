# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr = len(grid)
        nc = len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] =='1':
                self.dfs(grid, x, y)

    def numIslands(self, grid):
        # dfs深度优先搜索
        nums_lands = 0
        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    nums_lands += 1
                    self.dfs(grid, r, c)
        return nums_lands
# leetcode submit region end(Prohibit modification and deletion)
