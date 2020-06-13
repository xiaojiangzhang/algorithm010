//给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
//ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
//
// 说明：你不能倾斜容器，且 n 的值至少为 2。 
//
// 
//
// 
//
// 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
//
// 
//
// 示例： 
//
// 输入：[1,8,6,2,5,4,8,3,7]
//输出：49 
// Related Topics 数组 双指针


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    /*
            1.暴力解法：以此遍历所有柱子组成的容器的容量，取最大值
            时间复杂度：O(n^2)
            空间复杂度：O(1)
            2.缩小左右边界，初始边界为left = 0； right = height.length
            当左边界小于右边界时，left++
            当右边界小于左边界时，right--
            时间复杂度O（n）
            空间复杂度O（1）
            * */
    public int maxArea1(int[] height) {

        int maxArea = 0;
        for (int i = 0; i < height.length - 1; i++) {
            for (int j = i + 1; j < height.length; j++) {
                maxArea = Math.max(maxArea, (j - i) * Math.min(height[i], height[j]));
            }
        }
        return maxArea;
    }

    public int maxArea(int[] height) {
        int maxArea = 0;
        for (int i = 0, j = height.length - 1; i < j; ) {
            int minHeight = height[i] < height[j] ? height[i++] : height[j--];
            int area = (j - i +1) * minHeight;
            maxArea = Math.max(maxArea, area);
        }
        return maxArea;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
