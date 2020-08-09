# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  
# 
#  示例 1: 
# 
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1 
# 
#  示例 2: 
# 
#  输入: coins = [2], amount = 3
# 输出: -1 
# 
#  
# 
#  说明: 
# 你可以认为每种硬币的数量是无限的。 
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        递归暴力求解：
        """

        def dp(n):
            if n < 0:
                return -1
            if n == 0:
                return 0

            res = float("INF")
            for c in coins:
                subproblem = dp(n - c)
                if subproblem == -1:
                    continue
                else:
                    res = min(res, 1 + subproblem)
            return res if res != float("INF") else -1

        return dp(amount)



        # def dp(n):
        #     # 递归结束条件(超时) 假设dp（n）表示总金额为n时最少硬币数，res = min(res,dp（n-c)+1)
        #     if n < 0: return -1
        #     if n == 0: return 0
        #     res = float("INF")
        #     for c in coins:
        #         subproblem = dp(n - c)
        #         if subproblem == -1: continue
        #         res = min(res, 1 + subproblem)
        #     return res if res != float("INF") else -1
        # return dp(amount)

        # 记忆化搜索，递归优化
        # memo = dict()
        #
        # def dp(n):
        #     if n in memo: return memo[n]
        #     if n < 0:
        #         return -1
        #     if n == 0:
        #         return 0
        #     res = float("inf")
        #     for c in coins:
        #         subproblem = dp(n - c)
        #         if subproblem == -1:
        #             continue
        #         res = min(res, subproblem + 1)
        #     memo[n] = res if res != float('inf') else -1
        #     return memo[n]
        #
        # return dp(amount)

        # 动态规划
        # dp[i]表示当目标金额为i时，至少需要dp[i]枚硬币凑出
        # dp[i] = dp[i - c] + 1    base: dp[0] = 0
        # dp = [amount + 1 for i in range(amount + 1)]
        # dp[0] = 0
        # for i in range(amount + 1):
        #     for c in coins:
        #         if i - c < 0: continue
        #         dp[i] = min(dp[i], 1 + dp[i - c])
        # return dp[amount] if dp[amount] != amount + 1 else -1
