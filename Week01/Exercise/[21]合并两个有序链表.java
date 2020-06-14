
import java.util.HashMap.TreeNode;
import java.util.List;
import java.util.LinkedList;//将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
//
// 
//
// 示例： 
//
// 输入：1->2->4, 1->3->4
//输出：1->1->2->3->4->4
// 
// Related Topics 链表


//leetcode submit region begin(Prohibit modification and deletion)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    //    递归求解，当 l1.val<l2.val 时, 递归merge（l1, l2.next）;
//              否则执行merge（l1.next,l2）
//    复杂度分析:
//    时间复杂度：O(n + m)O(n+m)，其中 nn 和 mm 分别为两个链表的长度。
// 因为每次调用递归都会去掉 l1 或者 l2 的头节点（直到至少有一个链表为空），
// 函数 mergeTwoList 至多只会递归调用每个节点一次。因此，时间复杂度取决于合并后的链表长度，
// 即 O(n+m)O(n+m)。
//    空间复杂度：O(n + m)O(n+m)，其中 nn 和 mm 分别为两个链表的长度。
// 递归调用 mergeTwoLists 函数时需要消耗栈空间，栈空间的大小取决于递归调用的深度。
// 结束递归调用时 mergeTwoLists 函数最多调用 n+mn+m 次，因此空间复杂度为 O(n+m)O(n+m)。
//    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
//        if (l1 == null) return l2;
//        else if (l2 == null) return l1;
//        else if (l1.val < l2.val) {
//            l1.next = mergeTwoLists(l1.next, l2);
//            return l1;
//        } else {
//            l2.next = mergeTwoLists(l1, l2.next);
//            return l2;
//        }
    /*迭代求解
        时间复杂度：O（n）
        空间复杂度：O（1）
     * */
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode prehead = new ListNode(-1);
        ListNode prerev = prehead;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                prerev.next = l1;
                l1 = l1.next;
            } else {
                prerev.next = l2;
                l2 = l2.next;
            }
            prerev = prerev.next;
        }
        prerev.next = l1 == null ? l2 : l1;
        return prehead.next;

    }

//    迭代求解
}
//leetcode submit region end(Prohibit modification and deletion)
