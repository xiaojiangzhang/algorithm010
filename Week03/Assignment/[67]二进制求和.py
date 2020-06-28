# 给你两个二进制字符串，返回它们的和（用二进制表示）。 
# 
#  输入为 非空 字符串且只包含数字 1 和 0。 
# 
#  
# 
#  示例 1: 
# 
#  输入: a = "11", b = "1"
# carry = 0
# carry, cur = divmod(1+1+carry, 2) = （1,0）

# 输出: "100" 
# 
#  示例 2: 
# 
#  输入: a = "1010", b = "1011"
# 输出: "10101" 
# 
#  
# 
#  提示： 
# 
#  
#  每个字符串仅由字符 '0' 或 '1' 组成。 
#  1 <= a.length, b.length <= 10^4 
#  字符串如果不是 "0" ，就都不含前导零。 
#  
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 1、直接转十进制求解
        # return '{0:b}'.format(int(a, 2) + int(b, 2))
        # 2、每位相加
        a, b, ans = a[::-1], b[::-1], []
        i = j = carry = 0
        while i < len(a) or j < len(b) or carry:
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[j]) if j < len(b) else 0
            # carry 为除数 即进位的大小， cur为余数 即当前位置上的数
            carry, cur = divmod(n1 + n2 + carry, 2)
            ans.append(str(cur))
            i, j = i + 1, j + 1
        return ''.join(ans[::-1])
# leetcode submit region end(Prohibit modification and deletion)
