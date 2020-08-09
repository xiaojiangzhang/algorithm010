# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。 
# 
#  有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。 
# 
#  
# 
#  示例: 
# 
#  输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"] 
#  Related Topics 字符串 回溯算法 
#  👍 360 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def dfs(track, start, s):
            # 满四段，并且用光所有字符
            if len(track) == 4 and start == len(s):
                res.append(".".join(track))
            # 满四段但没用光所有字符
            if len(track) == 4 and start < len(s):
                return
            for i in range(1, 4):
                if start + i - 1 >= len(s):
                    return
                if i >= 2 and s[start] == '0':
                    return
                tmp = s[start:start + i]
                if i == 3 and int(tmp) > 255:
                    return
                dfs(track + [tmp], start + i, s)

        dfs([], 0, s)
        return res

# leetcode submit region end(Prohibit modification and deletion)
