# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 筛选非字母和数字的字符后，对字符串进行翻转，比较翻转后的两个字符串  时间O(n)  O（s）
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tar = "".join(ch.lower() for ch in s if ch.isalnum())
        return tar == tar[::-1]

    # 2、使用双指针夹逼遍历 时间复杂度O（n) 空间复杂度O（n）
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        target = "".join(ch.lower() for ch in s if ch.isalnum())
        i = 0,
        j = len(target) - 1
        while (i < j):
            if target[i] != target[j]:
                return False;
            i += 1
            j += 1
        return True;

    # 双指针优化空间复杂度
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while (left < right):
            while (left < right and not s[left].isalnum()):
                left += 1
            while (left < right and not s[right].isalnum()):
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
