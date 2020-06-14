package week01;

import java.util.Arrays;

import java.util.HashMap;

import java.util.Map;
import java.util.Stack;

public class largest_rectangle_in_histogram {

    public static int largestRectangleArea1(int[] heights) {

        int maxArea = 0;
        for (int i = 0; i < heights.length; i++) {
            int left = i - 1, right = i + 1;
            while (left > -1) {
                if (heights[left] < heights[i]) break;
                else {
                    --left;
                }
            }
            while (right < heights.length) {
                if (heights[right] < heights[i]) break;
                else {
                    right++;
                }
            }
            System.out.println(left + " " + right);
            int minHeight = Math.min(heights[left + 1], heights[right - 1]);
            minHeight = Math.min(minHeight, heights[i]);
            maxArea = Math.max(maxArea, (right - left - 1) * minHeight);
        }

        return maxArea;
    }

    public static int largestRectangleArea(int[] heights) {
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


    public static void main(String[] args) {
        System.out.println(largestRectangleArea(new int[]{1}));
    }

}
