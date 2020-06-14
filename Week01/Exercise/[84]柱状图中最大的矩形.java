//给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
//
// 求在该柱状图中，能够勾勒出来的矩形的最大面积。 
//
// 
//
// 
//
// 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
//
// 
//
// 
//
// 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
//
// 
//
// 示例: 
//
// 输入: [2,1,5,6,2,3]
//输出: 10 
// Related Topics 栈 数组


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    /*暴力解法、遍历图中的每一根柱子，再根据当前的柱子判断当前柱子所能构成的最大矩形
    * */
//    public int largestRectangleArea(int[] heights) {
//        int maxArea = 0;
//        for (int i = 0; i < heights.length; i++) {
//            int left = i - 1, right = i + 1;
//            while (left > -1) {
//                if (heights[left] < heights[i]) break;
//                else {
//                    --left;
//                }
//            }
//            while (right < heights.length) {
//                if (heights[right] < heights[i]) break;
//                else {
//                    right++;
//                }
//            }
//            System.out.println(left + " " + right);
//            int minHeight = Math.min(heights[left + 1], heights[right - 1]);
//            minHeight = Math.min(minHeight, heights[i]);
//            maxArea = Math.max(maxArea, (right - left - 1) * minHeight);
//        }
//
//        return maxArea;
//    }
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Stack<Integer> stack = new Stack<Integer>();
        int[] lefts = new int[n];
        int[] rights = new int[n];
        Arrays.fill(rights, n);
        for (int i = 0; i < n; ++i) {
            while (!stack.empty() && heights[stack.peek()] >= heights[i]) {
                rights[stack.peek()] = i;
                stack.pop();
            }
            lefts[i] = stack.empty() ? -1 : stack.peek();
            stack.push(i);
        }
        int area = 0;
        for (int i = 0; i < n; ++i) {
            area = Math.max(area, (rights[i] - lefts[i] - 1) * heights[i]);

        }
        return area;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
